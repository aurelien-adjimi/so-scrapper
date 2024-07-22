import pytest
from bs4 import BeautifulSoup

def test_html_parsing():
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
    soup = BeautifulSoup(html_content, 'html.parser')
    question = soup.find('div', id='question-summary-1')
    assert question is not None
