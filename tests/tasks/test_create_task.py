import json

class TestCreateTask:
    def test_create_task_success(self, client):
        # Update with the actual URL name
        task_data = {
            "title": "New Task",
            "description": "This is a test task."
        }

        response = client.post("/api/tasks/", data=json.dumps(task_data), content_type='application/json')

        # Check if the response is successful
        assert response.status_code == 201  # HTTP 201 Created
        response_data = json.loads(response.content)
        assert 'data' in response_data  # Ensure response contains data key
        assert response_data['data']['title'] == task_data['title']
        assert response_data['data']['description'] == task_data['description']

    def test_create_task_missing_required_fields(self, client):
        """
        Test case for when a required field (title) is missing.
        """
        data = {
            "description": "Missing title field"
        }
        response = client.post("/api/tasks/", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 400
        response_data = json.loads(response.content)
        assert "error" in response_data  # Ensure response contains error key
        assert "title" in response_data["error"][0]["loc"]  # Check for title error

    def test_create_task_empty_fields(self, client):
        """
        Test case for when the 'title' field is empty.
        """
        data = {
            "title": "",
            "description": "Empty title"
        }
        response = client.post("/api/tasks/", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 400
        response_data = json.loads(response.content)
        assert "error" in response_data
        assert "title" in response_data["error"][0]["loc"]  # Check for title error

    def test_create_task_invalid_data_type(self, client):
        """
        Test case for when the 'title' field has an invalid data type.
        """
        data = {
            "title": 123,  # Invalid type for title
            "description": "Invalid data type for title"
        }
        response = client.post("/api/tasks/", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 201  # HTTP 201 Created
        response_data = json.loads(response.content)
        assert 'data' in response_data  # Ensure response contains data key
        assert response_data['data']['title'] == str(data['title']) # check if title is converted to string
        assert response_data['data']['description'] == data['description']

    def test_create_task_too_long_fields(self, client):
        """
        Test case for when the 'title' field exceeds the maximum allowed length.
        """
        data = {
            "title": "A" * 256,  # Assuming the max length for title is 255 characters
            "description": "A valid description"
        }
        response = client.post("/api/tasks/", data=json.dumps(data), content_type='application/json')


        response_data = json.loads(response.content)
        assert response.status_code == 400
        assert "error" in response_data
        assert "title" in response_data["error"][0]["loc"]  # Check for title error

    def test_create_task_extra_fields(self, client):
        """
        Test case for when extra fields are passed in the request.
        """
        data = {
            "title": "Test Task",
            "description": "A valid test description",
            "extra_field": "This should be ignored"
        }
        response = client.post("/api/tasks/", data=json.dumps(data), content_type='application/json')

        assert response.status_code == 201
        response_data = json.loads(response.content)
        assert "data" in response_data
        assert "extra_field" not in response_data["data"]  # Ensure extra field is not returned


