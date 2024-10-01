from loguru import logger

from ..db_adapters import TaskDB
from ..schemas import TaskSchema

class TaskUsecase():
    def __init__(self):
        self.task_db = TaskDB()
        logger.info("TaskUsecase initialized.")

    def get_tasks(self, page=1, limit=10):
        """Retrieve a paginated list of tasks."""
        task_objs = self.task_db.get_tasks(page=page, limit=limit)
        if not task_objs:
            logger.error("No tasks found.")
            return {"error": "No tasks found"}, 404
        tasks_list = [TaskSchema.from_orm(task).dict() for task in task_objs]
        return {"data": tasks_list}, 200

    def get_task(self, task_id=None):
        """Retrieve a specific task by its ID."""
        task_obj = self.task_db.get_task(task_id=task_id)
        if not task_obj:
            logger.error(f"Task with task_id:{task_id} not found.")
            return {"error": "Task with task_id:{} not found".format(task_id)}, 404
        task_dict = TaskSchema.from_orm(task_obj).dict()
        return {"data": task_dict}, 200

    def create_task(self, data=None):
        """Create a new task with the provided data."""
        inserted_task_obj = self.task_db.create_task(data)
        if not inserted_task_obj:
            logger.error("Task cannot be created.")
            return {"error": "Task cannot be created"}, 404
        inserted_task_dict = TaskSchema.from_orm(inserted_task_obj).dict()
        return {"data": inserted_task_dict}, 201

    def update_task(self, task_id=None, data=None):
        """Update an existing task with the given ID and data."""
        updated_task_obj = self.task_db.update_task(task_id=task_id, data=data)
        if not updated_task_obj:
            logger.error(f"Task with task_id:{task_id} not found for update.")
            return {"error": "Task with task_id:{} not found".format(task_id)}, 404
        updated_task_dict = TaskSchema.from_orm(updated_task_obj).dict()
        return {"data": updated_task_dict}, 200

    def delete_task(self, task_id=None):
        """Delete a specific task by its ID."""
        deleted = self.task_db.delete_task(task_id=task_id)
        if not deleted:
            logger.error(f"Task with task_id:{task_id} not found for deletion.")
            return {"error": "Task with task_id:{} not found".format(task_id)}, 404
        return None, 204
