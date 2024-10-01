import pytest
import json
from django.urls import reverse

class TestGetTask:
    def test_get_task_success(self, client, create_task):  # Assuming you have a fixture to create a task
        """Test successful retrieval of a single task."""
        task_id = create_task["id"] # Use the ID of the created task
        response = client.get(f"/api/tasks/{task_id}/")

        assert response.status_code == 200  # HTTP 200 OK
        response_data = json.loads(response.content)
        assert 'data' in response_data  # Ensure response contains data key
        assert response_data['data']['id'] == task_id  # Check that the correct task ID is returned

    def test_get_task_not_found(self, client):
        """Test case for when a task with a given ID does not exist."""
        response = client.get("/api/tasks/999999/")  # Use a non-existing task ID

        assert response.status_code == 404  # HTTP 404 Not Found
        response_data = json.loads(response.content)
        assert 'error' in response_data  # Ensure response contains error key
        assert response_data['error'] == "Task with task_id:999999 not found"  # Check that the error message is appropriate

    def test_get_task_invalid_id(self, client):
        """Test case for when an invalid task ID is provided."""
        response = client.get("/api/tasks/invalid_id/")  # Use an invalid task ID format
        assert response.status_code == 404 # HTTP 404 Not Found


