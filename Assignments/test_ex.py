#for patch function create a 'json'(data.json) file in the same folder of source/test code

import json
from unittest.mock import patch


# Function to read data from a local JSON file
def get_data(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


# Mocking the `open` function to simulate reading a local JSON file
@patch('builtins.open')
@patch('json.load')
def test_get_data(mock_json_load, mock_open):
    # Mock the file content returned by `json.load`
    mock_json_load.return_value = {"key": "mocked_value"}

    # Call the function with a dummy file path
    result = get_data('data.json')

    # Assertions
    assert result == {"key": "mocked_value"}  # Verify the mocked data is returned
    mock_open.assert_called_once_with('data.json', 'r')  # Ensure the file was opened correctly
    mock_json_load.assert_called_once()  # Verify `json.load` was called


# Run the test function
if __name__ == "__main__":
    test_get_data()
    print("Test passed successfully!")
