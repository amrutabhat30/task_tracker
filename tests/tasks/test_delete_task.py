import pytest
import json
from django.urls import reverse


class TestDeleteTask:
    def test_delete_task_success(self, client, create_task):  # Assuming you have a fixture to create a task
        """Test successful deletion of a task."""
        task_id = create_task["id"]  # Use the ID of the created task

        response = client.delete(f"/api/tasks/{task_id}/")

        assert response.status_code == 204  # HTTP 204 No Content

    def test_delete_task_not_found(self, client):
        """Test case for when trying to delete a task that does not exist."""
        response = client.delete("/api/tasks/999999/")  # Using an ID that doesn't exist

        assert response.status_code == 404  # HTTP 404 Not Found
        response_data = json.loads(response.content)
        assert 'error' in response_data
        assert response_data['error'] == "Task with task_id:999999 not found"

    def test_delete_task_invalid_id(self, client):
        """Test case for when an invalid ID is provided for deletion."""
        response = client.delete("/api/tasks/invalid_id/")  # Using an invalid ID

        response = client.get("/api/tasks/invalid_id/")  # Use an invalid  ID
        assert response.status_code == 404  # HTTP 404 Not Found


