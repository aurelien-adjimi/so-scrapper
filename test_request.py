import pytest
from unittest.mock import patch, MagicMock
import requests 

@patch('requests.get')
def test_http_request(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = '<html></html>'
    mock_get.return_value = mock_response

    response = requests.get('https://stackoverflow.com/questions')
    assert response.status_code == 200
    assert response.text == '<html></html>'
