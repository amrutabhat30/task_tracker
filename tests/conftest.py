import pytest
from django.test import Client
import json

@pytest.fixture
def client():
    """
    Fixture to provide a test client.
    This will be available across all test files.
    """
    return Client()


@pytest.fixture
def create_task(client):
    """
    Fixture to create a task and return the response.
    """
    task_data = {
        "title": "Fixture Task",
        "description": "This task is created for testing purposes."
    }

    response = client.post("/api/tasks/", data=json.dumps(task_data), content_type='application/json')

    assert response.status_code == 201  # Ensure the task was created successfully
    return response.json()['data']  # Return the created task data