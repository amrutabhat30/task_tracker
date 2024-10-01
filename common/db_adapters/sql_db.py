from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError, NoResultFound, OperationalError
from datetime import datetime, timezone
from loguru import logger

from server.settings import SQL_DETAILS


class SQLDB:
    """
    DB class responsible for managing database connection and session lifecycle.
    It provides methods for getting and closing sessions, as well as executing queries.
    """

    def __init__(self):
        """
        Initializes the SQLDB class with a given database URL and creates a connection engine.
        """
        self.db_url = (
            "mysql+pymysql://" +
            SQL_DETAILS.get("USER", '') + ":" +
            SQL_DETAILS.get("PASSWORD", '') + "@" +
            SQL_DETAILS.get("HOST", '') + ":" +
            SQL_DETAILS.get("PORT", '') + "/" +
            SQL_DETAILS.get("DB_NAME", '')
        )
        logger.debug(f"Database URL: {self.db_url}")
        self.engine = create_engine(self.db_url)

    def get_connection(self):
        """
        Establishes a connection to the database.

        Returns:
            connection: SQLAlchemy connection object.
        """
        logger.info("Establishing a new database connection.")
        return self.engine.connect()

    def close_connection(self, connection):
        """
        Closes the given database connection.

        Args:
            connection: SQLAlchemy connection object to be closed.
        """
        logger.info("Closing the database connection.")
        connection.close()

    def execute_query(self, query, params=None):
        """
        Executes a given SQL query with parameters, managing the connection manually.

        Args:
            query (str): The SQL query to execute.
            params (dict, optional): The parameters to bind to the query.

        Returns:
            result: The result of the query execution or an error message.
        """
        logger.debug(f"Executing query: {query} with params: {params}")
        connection = self.get_connection()
        try:
            result = connection.execute(text(query), params)
            if result.rowcount > 0:
                logger.info("Query executed successfully; committing changes.")
                connection.commit()
            return result
        except SQLAlchemyError as e:
            logger.error(f"SQLAlchemy error occurred: {str(e)}")
            return str(e)  # Return the error message as a string
        finally:
            self.close_connection(connection)

    def set_clause(self, data):
        """Generates a SET clause string and parameters."""
        set_clause = ', '.join([f"{key} = :{key}" for key in data.keys()])
        logger.debug(f"Generated SET clause: {set_clause}")
        return set_clause, data

    def where_clause(self, where):
        """Generates a WHERE clause string and parameters."""
        where_clause = ' AND '.join([f"{key} = :{key}" for key in where.keys()])
        logger.debug(f"Generated WHERE clause: {where_clause}")
        return where_clause, where

    def insert(self, table, data):
        """Inserts a record into the specified table.

        Args:
            table (str): The name of the table.
            data (dict): The data to insert.

        Returns:
            tuple or str: The inserted row as a dictionary or an error message.
        """
        logger.info(f"Inserting data into {table}: {data}")
        data['created_at'] = datetime.now(timezone.utc)
        data['updated_at'] = datetime.now(timezone.utc)

        columns = ', '.join(data.keys())
        placeholders = ', '.join([f":{key}" for key in data.keys()])

        query = f'INSERT INTO {table} ({columns}) VALUES ({placeholders})'

        # Execute the insert operation
        result = self.execute_query(query, data)

        if isinstance(result, str):  # If it's an error message
            logger.error(f"Failed to insert data into {table}: {result}")
            raise OperationalError(f"Failed to insert a new task: {result}")

        # Fetch the last inserted row based on the primary key (assuming the primary key is 'id')
        last_inserted_id = result.lastrowid  # Get the last inserted ID (for SQLite)

        logger.info(f"Fetching the inserted row with ID: {last_inserted_id}")
        return self.fetch_one(table, {'id': last_inserted_id})  # Fetch and return the inserted row

    def update(self, table, data, where):
        """Updates a record in the specified table.

        Args:
            table (str): The name of the table.
            data (dict): The data to update.
            where (dict): The condition for the update.

        Returns:
            int: The number of updated rows or an error message.
        """
        logger.info("Updating record in database.")
        logger.debug(f"Update data: {data}, where condition: {where}")
        data['updated_at'] = datetime.now(timezone.utc)
        set_clause, set_params = self.set_clause(data)
        where_clause, where_params = self.where_clause(where)

        query = f'UPDATE {table} SET {set_clause} WHERE {where_clause}'
        params = {**set_params, **where_params}
        logger.debug(f"Update DB query: {query} with params: {params}")

        result = self.execute_query(query, params)
        if isinstance(result, str):  # If it's an error message
            logger.error(f"Failed to update record in {table}: {result}")
            raise OperationalError(f"Failed to update the task with {where.get('task_id')} and {result}")
        logger.info("Record updated successfully.")
        return self.fetch_one(table, where)

    def delete(self, table, where):
        """Deletes a record in the specified table.

        Args:
            table (str): The name of the table.
            where (dict): The condition for the deletion.

        Returns:
            int: The number of deleted rows or an error message.
        """
        logger.info("Deleting record from database.")
        where_clause, where_params = self.where_clause(where)

        query = f'DELETE FROM {table} WHERE {where_clause}'
        logger.debug(f"Delete DB query: {query} with params: {where_params}")
        result = self.execute_query(query, where_params)
        if isinstance(result, str):  # If it's an error message
            logger.error(f"No record found in table '{table}' with {where}: {result}")
            raise NoResultFound(f"No record found in table '{table}' with {where}: {result}")
        logger.info("Record deleted successfully.")
        return result.rowcount > 0

    def fetch_one(self, table, where):
        """Fetches a single record from the specified table.

        Args:
            table (str): The name of the table.
            where (dict): The condition for fetching.

        Returns:
            tuple or str: The fetched row or an error message.
        """
        logger.info("Fetching a single record from the database.")
        where_clause, where_params = self.where_clause(where)
        query = f'SELECT * FROM {table} WHERE {where_clause}'
        logger.debug(f"FETCH ONE DB query: {query} with params: {where_params}")
        result = self.execute_query(query, where_params)
        if isinstance(result, str):  # If it's an error message
            logger.error(f"No record found in table '{table}' with {where}: {result}")
            raise NoResultFound(f"No record found in table '{table}' with {where}: {result}")
        logger.info("Record fetched successfully.")
        return result.fetchone()  # Return the fetched row

    def fetch_all(self, table, where, page=1, limit=10):
        """Fetches all records from the specified table.

        Args:
            table (str): The name of the table.

        Returns:
            list or str: The list of fetched rows or an error message.
        """
        logger.info("Fetching all records from the database.")
        offset = (page - 1) * limit
        where_clause, where_params = self.where_clause(where)
        query = f'SELECT * FROM {table} WHERE {where_clause} LIMIT {limit} OFFSET {offset}'
        logger.debug(f"FETCH ALL DB query: {query} with params: {where_params}")
        result = self.execute_query(query, where_params)
        if isinstance(result, str):  # If it's an error message
            logger.error(f"No records found in table '{table}': {result}")
            raise NoResultFound(f"No record found in table '{table}': {result}")
        logger.info("All records fetched successfully.")
        return result.fetchall()  # Return the fetched rows
