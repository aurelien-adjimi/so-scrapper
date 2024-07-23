### Imports ###
import pytest
from unittest.mock import patch, MagicMock
from scraping_scripts.scrapping import scrape_with_beautifulsoup

@patch('scrapping.requests.get') # J'utilise le décorateur patch pour remplacer la fonction requests.get par un objet factice mock_get dans le module scrapping. Cela permet de simuler les appels HTTP pendant le test.
def test_data_extraction_with_beautifulsoup(mock_get):
    mock_response = MagicMock() # Crée un objet MagicMock pour simuler une réponse HTTP.
    mock_response.status_code = 200 # Définit le code de statut de la réponse factice à 200 pour indiquer un succès.
    # Définit le contenu HTML de la réponse factice pour représenter une question Stack Overflow avec des attributs et des éléments spécifiques.
    mock_response.text = """ 
    <div id="question-summary-1">
        <h3><a class="question-hyperlink" href="/questions/1">Question Title</a></h3>
        <div class="s-post-summary--content-excerpt">Summary of the question</div>
        <a class="post-tag">tag1</a>
        <a class="post-tag">tag2</a>
        <div class="s-user-card--link"><a>Author</a></div>
        <span class="relativetime" title="2024-07-18 08:15:13Z"></span>
        <div class="s-post-summary--stats-item">
            <span class="s-post-summary--stats-item-number">10</span>
        </div>
        <div class="s-post-summary--stats-item">
            <span class="s-post-summary--stats-item-number">5</span>
        </div>
        <div class="s-post-summary--stats-item">
            <span class="s-post-summary--stats-item-number">100</span>
        </div>
    </div>
    """
    mock_get.return_value = mock_response # Définit la valeur de retour de l'appel mock_get pour qu'elle soit la réponse factice mock_response.

    data = scrape_with_beautifulsoup(max_pages=1) # Appelle la fonction scrape_with_beautifulsoup pour scraper les données, en limitant à une seule page.
    # Les assertions sont là pour vérifier que les données extraites correspondent bien aux valeurs attendues
    assert len(data) == 1
    assert data[0]['title'] == 'Question Title'
    assert data[0]['summary'] == 'Summary of the question'
    assert data[0]['tags'] == ['tag1', 'tag2']
    assert data[0]['author'] == 'Author'
    assert data[0]['date'] == '2024-07-18 08:15:13Z'
    assert data[0]['votes'] == '10'
    assert data[0]['answers'] == '5'
    assert data[0]['views'] == '100'
