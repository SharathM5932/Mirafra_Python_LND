import pytest
import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

# Pytest fixture to return the base URL
@pytest.fixture
def api_base_url():
    return BASE_URL

# Test Case 1: Verify GET Request using Fixture
def test_get_todo(api_base_url):
    response = requests.get(f"{api_base_url}/todos/1")
    assert response.status_code == 200  # Check if response is 200 OK
    json_data = response.json()
    assert json_data["id"] == 1
    assert "title" in json_data
    assert isinstance(json_data["completed"], bool)

# Test Case 2: Verify POST Request using Fixture
@pytest.fixture
def new_post_data():
    return {
        "title": "Hello, World!",
        "body": "This is a test post.",
        "userId": 1
    }

def test_create_post(api_base_url, new_post_data):
    url = f"{api_base_url}/posts"
    response = requests.post(url, json=new_post_data)
    assert response.status_code == 201  # HTTP 201 Created
    json_data = response.json()
    assert json_data["title"] == new_post_data["title"]
    assert json_data["body"] == new_post_data["body"]
    assert json_data["userId"] == new_post_data["userId"]
    assert "id" in json_data  # Ensure ID is returned

# Test Case 3: Verify Invalid GET Request
def test_invalid_get_request(api_base_url):
    response = requests.get(f"{api_base_url}/todos/99999")
    assert response.status_code == 404  # Should return 404 Not Found

# Test Case 4: Verify Invalid POST Request (Missing Required Fields)
def test_invalid_post_request(api_base_url):
    url = f"{api_base_url}/posts"
    data = {}  # Empty payload

    response = requests.post(url, json=data)
    assert response.status_code in [400, 422]  # Expecting client error
