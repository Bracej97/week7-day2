from unittest.mock import patch
import requests

def fetch_data(url):
    """Function to fetch data from an API endpoint."""
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
    print(response)
    return response.json()

@patch('requests.get')
def test_fetch_data_mocked(mock_get):
    """Test the fetch_data function with mocking."""
    # Arrange: Set up the mock to return a specific response
    mock_get.return_value.json.return_value = {'id': 1, 'title': 'Mocked Title'}

    # Act: Call the function under test
    url = "https://catfact.ninja/fact"
    data = fetch_data(url)

    # Assert: Check the results
    assert data['id'] == 1
    assert data['title'] == 'Mocked Title'
    mock_get.assert_called_once_with(url)
