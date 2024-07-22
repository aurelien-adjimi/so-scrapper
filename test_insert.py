import pytest
from unittest.mock import patch, MagicMock
from database import save_to_mongo

@patch('pymongo.collection.Collection.insert_many')
def test_data_insertion_to_mongo(mock_insert_many):
    data = [{
        'title': 'Question Title',
        'link': 'https://stackoverflow.com/questions/1',
        'summary': 'Summary of the question',
        'tags': ['tag1', 'tag2'],
        'author': 'Author',
        'date': '2024-07-18 08:15:13Z',
        'votes': '10',
        'answers': '5',
        'views': '100'
    }]
    
    save_to_mongo(data)
    mock_insert_many.assert_called_once_with(data)
