# Standard library imports
import ujson
import sys

# Third-party imports
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from loguru import logger
from pydantic import ValidationError
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework.views import APIView
from rest_framework.response import Response

# Local application/library specific imports
from ..schemas.task_schema import TaskSchema
from common.schemas import PaginationSchema
from ..usecases import TaskUsecase

logger.add(sys.stderr, format="{time} {level} {message}", level="INFO")

@method_decorator(csrf_exempt, name='dispatch')
class TaskView(APIView):
    def __init__(self):
        # Initialize the TaskUsecase for handling task-related operations.
        self.task_usecase = TaskUsecase()
        logger.info("Initialized TaskView with TaskUsecase.")

    @swagger_auto_schema(
        operation_summary="Retrieve tasks",
        operation_description="Handles GET requests to retrieve tasks. "
                              "If task_id is provided, retrieves a specific task. "
                              "Otherwise, retrieves a paginated list of tasks.",
        manual_parameters=[
            openapi.Parameter('page', openapi.IN_QUERY,
                              description="Page number for pagination",
                              type=openapi.TYPE_INTEGER,
                              required=False),
            openapi.Parameter('limit', openapi.IN_QUERY,
                              description="Limit number of tasks per page",
                              type=openapi.TYPE_INTEGER,
                              required=False)
        ],
        responses={
            200: "List of tasks or a specific task based on task_id.",
            400: "Bad Request if pagination parameters are invalid.",
            404: "Task not found if task_id is specified."
        }
    )
    def get(self, request, task_id=None):
        """
        Handles GET requests to retrieve tasks. If task_id is provided,
        retrieves a specific task. Otherwise, retrieves a paginated list of tasks.

        :param request: The HTTP request object.
        :param task_id: Optional; the ID of the specific task to retrieve.
        :return: Response containing task data or an error message.
        """
        logger.debug(f"GET request received with task_id: {task_id}")

        if not task_id:
            # If no task_id is specified, handle pagination for the task list.
            page = request.GET.get("page", "1")
            limit = request.GET.get("limit", "10")

            logger.debug(f"Pagination parameters - Page: {page}, Limit: {limit}")

            # Validate page and limit parameters.
            if not page or not page.isdigit():
                page = 1
            if not limit or not limit.isdigit():
                limit = 10
            page = int(page)
            limit = int(limit)

            query_params = {"page": page, "limit": limit}
            try:
                # Validate pagination parameters using Pydantic schema.
                validated_data = PaginationSchema(**query_params)
                logger.info(f"Validated pagination data: {validated_data}")
            except ValidationError as e:
                # Return error response if validation fails.
                logger.error(f"Pagination validation error: {e.errors()}")
                return Response({'error': e.errors()}, status=400)

            logger.info(f"Fetching all tasks with pagination: Page {validated_data.page}, Limit {validated_data.limit}")
            # Fetch tasks using the validated page and limit.
            response, status_code = self.task_usecase.get_tasks(page=validated_data.page, limit=validated_data.limit)
        else:
            # If task_id is provided, fetch the specific task.
            try:
                task_id = int(task_id)  # Convert to int; raises ValueError if not possible
            except ValueError:
                return Response({'error': 'task_id must be an integer'}, status=400)
            logger.info(f"Fetching task with ID: {task_id}")
            response, status_code = self.task_usecase.get_task(task_id=task_id)

        logger.debug(f"Response for GET request: {response}")
        return Response(response, status=status_code, content_type="application/json")

    @swagger_auto_schema(
        operation_summary="Create a new task",
        operation_description="Handles POST requests to create a new task. "
                              "Requires task data in the request body. "
                              "On successful creation, returns the created task details.",
        responses={
            201: "Task Created.",
            400: "Validation error if the request data is invalid."
        }
    )
    def post(self, request):
        """
        Handles POST requests to create a new task.

        :param request: The HTTP request object containing task data.
        :return: Response containing created task data or an error message.
        """
        logger.debug(f"POST request received with body: {request.body}")
        try:
            # Parse the request body into TaskSchema.
            task_data = TaskSchema.parse_raw(request.body)
            logger.info(f"Parsed task data: {task_data}")

            # Create a new task using the task_usecase.
            response, status_code = self.task_usecase.create_task(data=task_data.dict())
            logger.info(f"Task created successfully: {response}")
            return Response(response, status=status_code, content_type="application/json")
        except ValidationError as e:
            # Return error response if validation fails.
            logger.error(f"Task creation validation error: {e.errors()}")
            return Response({'error': e.errors()}, status=400)

    @swagger_auto_schema(
        operation_summary="Update an existing task",
        operation_description="Handles PUT requests to update an existing task. "
                              "Requires task ID in the URL and updated task data in the request body. "
                              "Returns the updated task details.",
        responses={
            200: "Task Updated.",
            400: "Validation error if the request data is invalid.",
            404: "Task not found if the task_id does not exist."
        }
    )
    def put(self, request, task_id):
        """
        Handles PUT requests to update an existing task.

        :param request: The HTTP request object containing updated task data.
        :param task_id: The ID of the task to update.
        :return: Response containing updated task data or an error message.
        """
        logger.debug(f"PUT request received for task_id: {task_id} with body: {request.body}")
        try:
            # Load request body data using ujson for performance.
            data = ujson.loads(request.body)
            data["id"] = task_id

            # Validate the data against TaskSchema, excluding unset fields.
            validated_data = TaskSchema(**data).dict(exclude_unset=True)
            logger.info(f"Validated data for update: {validated_data}")

            # Update the task using the task_usecase.
            response, status_code = self.task_usecase.update_task(task_id=task_id, data=validated_data)
            logger.info(f"Task updated successfully: {response}")
            return Response(response, status=status_code, content_type="application/json")
        except ValidationError as e:
            # Return error response if validation fails.
            logger.error(f"Task update validation error: {e.errors()}")
            return Response({'error': e.errors()}, status=400)

    @swagger_auto_schema(
        operation_summary="Delete a specific task",
        operation_description="Handles DELETE requests to remove a specific task by ID. "
                              "Returns a confirmation message upon successful deletion.",
        responses={
            204: "Task deleted",
            404: "Task not found if the task_id does not exist."
        }
    )
    def delete(self, request, task_id):
        """
        Handles DELETE requests to remove a specific task.

        :param request: The HTTP request object.
        :param task_id: The ID of the task to delete.
        :return: Response containing the result of the deletion.
        """
        logger.debug(f"DELETE request received for task_id: {task_id}")
        response, status_code = self.task_usecase.delete_task(task_id=task_id)
        logger.info(f"Task deletion response: {response}")
        return Response(response, status=status_code, content_type="application/json")
