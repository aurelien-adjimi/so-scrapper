### Imports ###
import pytest
from unittest.mock import patch, MagicMock
from bdd.database import save_to_mongo

@patch('pymongo.collection.Collection.insert_many') # J'utilise le décorateur patch pour remplacer la méthode insert_many de la classe Collection de pymongo par un objet factice mock_insert_many. Cela permet de simuler l'insertion de données dans MongoDB pendant le test.
def test_data_insertion_to_mongo(mock_insert_many):
    # Crée une liste contenant un dictionnaire avec des données factices représentant une question Stack Overflow. Ces données incluent le titre, le lien, le résumé, les tags, l'auteur, la date, les votes, les réponses et les vues.
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
    
    save_to_mongo(data) # Appelle la fonction save_to_mongo avec les données factices data. Cette fonction est censée insérer les données dans MongoDB.
    mock_insert_many.assert_called_once_with(data) # Vérifie que la méthode insert_many a été appelée une seule fois avec les données data comme argument. Cela confirme que les données ont été correctement passées pour insertion dans MongoDB.
