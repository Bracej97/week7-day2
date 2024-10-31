# ----------------------------
# Introduction to Mocking
# ----------------------------

# This script demonstrates the concept of mocking in Python testing 
# using the unittest.mock module. It shows how to isolate tests from 
# external dependencies like API calls or database interactions.

# ----------------------------
# Step 1: Sample Function with External Dependency
# ----------------------------

import requests

def fetch_data(url):
    """Function to fetch data from an API endpoint."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    return response.json()

# ----------------------------
# Step 2: Writing Tests without Mocking (for illustration)
# ----------------------------

def test_fetch_data():
    """Test the fetch_data function without mocking (not recommended)."""
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = fetch_data(url)
    assert data['id'] == 1  # Check that the fetched data has id = 1

# ----------------------------
# Step 3: Mocking the External Dependency
# ----------------------------

from unittest.mock import patch

@patch('requests.get')
def test_fetch_data_mocked(mock_get):
    """Test the fetch_data function with mocking."""
    # Arrange: Set up the mock to return a specific response
    mock_get.return_value.json.return_value = {'id': 1, 'title': 'Mocked Title'}
    
    # Act: Call the function under test
    url = "https://jsonplaceholder.typicode.com/posts/1"
    data = fetch_data(url)

    # Assert: Check the results
    assert data['id'] == 1
    assert data['title'] == 'Mocked Title'
    mock_get.assert_called_once_with(url)  # Ensure the mock was called with the correct URL

# To run the tests in this file, use the following command:
# $ pytest example.py