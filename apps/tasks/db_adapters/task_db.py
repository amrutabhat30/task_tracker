from common.db_adapters.sql_db import SQLDB


class TaskDB(SQLDB):
    def __init__(self):
        super().__init__()
        self.table_name = "tasks"

    def create_task(self, task_data):
        """
        Creates a new task in the database.

        Parameters:
            task_data (dict): A dictionary containing the task details such as title, description, etc.

        Returns:
            dict: The inserted task details, including its ID and timestamps.

        Raises:
            Exception: Raises an exception if the task creation fails due to operational errors.
        """
        return self.insert(self.table_name, task_data)

    def update_task(self, task_id, data):
        """
        Updates an existing task in the database by task ID.

        Parameters:
            task_id (int): The ID of the task to be updated.
            data (dict): A dictionary containing updated task details.

        Returns:
            int: The number of rows affected by the update operation.

        Raises:
            Exception: Raises an exception if the task ID does not exist or the update fails.
        """
        where_clause = {'id': task_id, "deleted": False}
        return self.update(self.table_name, data, where_clause)

    def delete_task(self, task_id):
        """
        Marks a task as deleted in the database by task ID.

        Parameters:
            task_id (int): The ID of the task to delete.

        Returns:
            int: The number of rows affected by the delete operation.

        Raises:
            Exception: Raises an exception if the task ID does not exist or deletion fails.
        """
        where_clause = {'id': task_id, "deleted": False}
        return self.delete(self.table_name, where_clause)

    def get_task(self, task_id):
        """
        Retrieves a single task from the database by its ID.

        Parameters:
            task_id (int): The ID of the task to fetch.

        Returns:
            dict: The details of the task if found.

        Raises:
            Exception: Raises an exception if the task ID does not exist.
        """
        where_clause = {'id': task_id, "deleted": False}
        return self.fetch_one(self.table_name, where_clause)

    def get_tasks(self, page=1, limit=10):
        """
        Retrieves a paginated list of tasks from the database.

        Parameters:
            page (int): The page number for pagination. Defaults to 1.
            limit (int): The maximum number of tasks to retrieve per page. Defaults to 10.

        Returns:
            list: A list of tasks that are not marked as deleted.

        Raises:
            Exception: Raises an exception if the task retrieval fails due to operational errors.
        """
        where_clause = {"deleted": False}
        return self.fetch_all(self.table_name, where_clause, page=page, limit=limit)
