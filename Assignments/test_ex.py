
import pytest
import requests

# response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
# print(response.status_code)  # HTTP status code (e.g., 200 for success)
# print(response.json())

# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "title": "Hello, World!",
#     "body": "This is a test post.",
#     "userId": 1
# }
#
# response = requests.post(url, json=data)
# print(response.status_code)
# print(response.json())

def test_get_users():
    # Send GET request to the API
    response = requests.get("http://jsonplaceholder.typicode.com/users")

    # Check if the response status is 200 OK
    assert response.status_code == 200, "Failed to fetch users"

    # Parse JSON response and verify its content
    users = response.json()
    assert len(users) > 0, "No users found!"
    assert "name" in users[0], "Name field is missing in response"

    print("API Test Passed!")


# Calling the correct test function for API Testing
test_get_users()


