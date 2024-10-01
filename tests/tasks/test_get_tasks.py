import pytest
import json
from django.urls import reverse


class TestGetTasks:
    def test_get_tasks_success(self, client):
        """Test successful retrieval of tasks."""
        response = client.get("/api/tasks/")

        assert response.status_code == 200  # HTTP 200 OK
        response_data = json.loads(response.content)
        assert 'data' in response_data  # Ensure response contains data key
        assert isinstance(response_data['data'], list)  # Check that 'data' is a list

    # def test_get_tasks_empty(self, client):
    #     """Test retrieval when no tasks are available."""
    #     response = client.get("/api/tasks/")
    #
    #     assert response.status_code == 200  # HTTP 200 OK
    #     response_data = json.loads(response.content)
    #     assert 'data' in response_data  # Ensure response contains data key
    #     assert response_data['data'] == []  # Expect an empty list

    def test_get_tasks_with_pagination(self, client):
        """Test retrieval of tasks with pagination parameters."""
        response = client.get("/api/tasks/?page=1&limit=5")

        assert response.status_code == 200  # HTTP 200 OK
        response_data = json.loads(response.content)
        assert 'data' in response_data  # Ensure response contains data key
        assert isinstance(response_data['data'], list)  # Check that 'data' is a list
        assert len(response_data['data']) <= 5  # Check that length is less than or equal to limit

    def test_get_tasks_invalid_page(self, client):
        """Test case for when an invalid page number is provided."""
        response = client.get("/api/tasks/?page=-1&limit=5")  # Negative page number
        response_data = json.loads(response.content)
        assert response.status_code == 200  # H HTTP 200 OK negative page is ignored and default values rae considered
        response_data = json.loads(response.content)
        assert 'data' in response_data  # Ensure response contains data key
        assert isinstance(response_data['data'], list)  # Check that 'data' is a list
        assert len(response_data['data']) <= 5

    def test_get_tasks_invalid_limit(self, client):
        """Test case for when an invalid limit is provided."""
        response = client.get("/api/tasks/?page=1&limit=0")  # Limit of 0

        assert response.status_code == 400  # HTTP 400 Bad Request
        response_data = json.loads(response.content)
        assert 'error' in response_data  # Ensure response contains error key
        assert "limit" in response_data["error"][0]["loc"] # Check that the error mentions 'limit'

    def test_get_tasks_invalid_filter(self, client):
        """Test case for when an invalid filter parameter is provided."""
        response = client.get("/api/tasks/?invalid_filter=value")  # Invalid filter

        assert response.status_code == 200  # HTTP 200 OK
        response_data = json.loads(response.content)
        assert 'data' in response_data  # Ensure response contains data key
        assert isinstance(response_data['data'], list)  # Check that 'data' is a list
        assert len(response_data['data']) <= 10  # Check that length is less than or equal to default limit 10
