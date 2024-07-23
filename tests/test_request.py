### Imports ###
import pytest
from unittest.mock import patch, MagicMock
import requests 

@patch('requests.get') # Je me sers du décorateur 'patch' afin de remplacer temporairement la fonction get de request par un mock pendant l'exécution de la fonction de test. Ce qui permet de simuler un appel a requests.get sans effectuer véritablement la requête. 
def test_http_request(mock_get):
    mock_response = MagicMock() # Je crée un mock 
    mock_response.status_code = 200 # Je configure l'objet afin qu'il retourne un statut HTTP 200
    mock_response.text = '<html></html>' # Je configure l'objet mock pour qu'il retourne le texte HTML 
    mock_get.return_value = mock_response # Je configure le mock de requests.get pour qu'il retourne mock_response lorsque requests.get est appelé.

    response = requests.get('https://stackoverflow.com/questions') # J'appelle requests.get avec l'URL, grâce à patch, cet appel utilise le mock de requests.get et retourne mock_response.
    assert response.status_code == 200 # Je vérifie que le code de statut de la réponse est bien 200.
    assert response.text == '<html></html>' # Je vérifie que le texte de la réponse est bien '<html></html>'.
