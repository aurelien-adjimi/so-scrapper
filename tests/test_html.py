### Imports ###
import pytest
from bs4 import BeautifulSoup

def test_html_parsing():
    # Je définit une chaîne de caractères contenant un extrait HTML. 
    # Cet extrait représente une structure typique de question sur Stack Overflow, avec des balises et des attributs HTML spécifiques.
    html_content = """
    <div id="question-summary-1">
        <h3><a class="question-hyperlink" href="/questions/1">Question Title</a></h3>
        <div class="excerpt">Summary of the question</div>
        <a class="post-tag">tag1</a>
        <a class="post-tag">tag2</a>
        <div class="user-details"><a>Author</a></div>
        <span class="relativetime" title="2024-07-18 08:15:13Z"></span>
    </div>
    """
    soup = BeautifulSoup(html_content, 'html.parser') # J'utilise BeautifulSoup pour analyser la chaîne de caractères 'html_content'. 'html_parser' spécifie l'analyseur a utiliser
    question = soup.find('div', id='question-summary-1') # Je trouve la balise mère qui contient toutes les informations
    assert question is not None # Je vérifie que l'élément 'question' n'est pas None, ce qui signifie que la balise <div> avec l'id question-summary-1 a été trouvée avec succès dans le document HTML.
