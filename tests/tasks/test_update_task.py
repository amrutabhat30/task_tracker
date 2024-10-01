
import json

class TestUpdateTask:
    def test_update_task_success(self, client):
        """Test successful update of a task."""
        # Assume a task with ID 1 exists
        task_data = {
            "title": "Updated Task",
            "description": "This is an updated test task."
        }
        response = client.put("/api/tasks/23/", data=task_data, content_type='application/json')

        assert response.status_code == 200  # HTTP 200 OK
        response_data = json.loads(response.content)
        assert 'data' in response_data  # Ensure response contains data key
        assert response_data['data']['title'] == task_data['title']
        assert response_data['data']['description'] == task_data['description']

    def test_update_task_missing_required_fields(self, client):
        """Test case for when a required field (title) is missing."""
        data = {
            "description": "Missing title field"
        }
        response = client.put("/api/tasks/26/", data=data, content_type='application/json')

        assert response.status_code == 400
        assert "error" in response.json()  # Error details in 'error'
        assert "title" in response.json()["error"][0]["loc"]

    def test_update_task_empty_fields(self, client):
        """Test case for when the 'title' field is empty."""
        data = {
            "title": "",
            "description": "Empty title"
        }
        response = client.put("/api/tasks/27/", data=data, content_type='application/json')

        assert response.status_code == 400
        assert "error" in response.json()
        assert "title" in response.json()["error"][0]["loc"]

    def test_update_task_invalid_data_type(self, client):
        """Test case for when the 'title' field has an invalid data type."""
        data = {
            "title": 123,  # Invalid type for title
            "description": "Invalid data type for title"
        }
        response = client.put("/api/tasks/28/", data=data, content_type='application/json')

        assert response.status_code == 200  # HTTP 201 Created
        response_data = json.loads(response.content)
        assert 'data' in response_data  # Ensure response contains data key
        assert response_data['data']['title'] == str(data['title'])  # check if title is converted to string
        assert response_data['data']['description'] == data['description']

    def test_update_task_too_long_fields(self, client):
        """Test case for when the 'title' field exceeds the maximum allowed length."""
        data = {
            "title": "A" * 256,  # Assuming the max length for title is 255 characters
            "description": "A valid description"
        }
        response = client.put("/api/tasks/29/", data=data, content_type='application/json')

        assert response.status_code == 400
        assert "error" in response.json()
        assert "title" in response.json()["error"][0]["loc"]

    def test_update_task_extra_fields(self, client):
        """Test case for when extra fields are passed in the request."""
        data = {
            "title": "Test Task",
            "description": "A valid test description",
            "extra_field": "This should be ignored"
        }
        response = client.put("/api/tasks/32/", data=data, content_type='application/json')

        assert response.status_code == 200  # Assuming update is successful
        assert "data" in response.json()
        assert "extra_field" not in response.json()["data"]

    def test_update_task_invalid_id(self, client):
        """Test case for when an invalid task ID is provided."""
        data = {
            "title": "Test Task",
            "description": "A valid description"
        }
        response = client.put("/api/tasks/9999/", data=data, content_type='application/json')  # Assume 9999 does not exist

        assert response.status_code == 404
        assert "error" in response.json()  # Error details in 'error'
        assert "not found" in response.json()["error"]  # Example error message

    def test_update_task_not_found(self, client):
        """Test case for updating a non-existent task."""
        data = {
            "title": "Test Task",
            "description": "A valid description"
        }
        response = client.put("/api/tasks/9999/", data=data, content_type='application/json')  # Assume 9999 does not exist

        assert response.status_code == 404
        assert "error" in response.json()  # Error details in 'error'
        assert "not found" in response.json()["error"]
