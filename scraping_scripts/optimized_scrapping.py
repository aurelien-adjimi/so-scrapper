### Imports ###
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed


### Fonction pour récupérer le contenu HTML d'une page web ###
def fetch_page(url):
    try:
        response = requests.get(url) # Effectue une requête HTTP GET pour obtenir le contenu de l'URL spécifiée.
        response.raise_for_status() # Lève une exception si la requête échoue (par exemple, en cas de code d'état HTTP 404 ou 500).
        return response.text # Retourne le contenu HTML de la page en cas de succès.
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None

### Fonction pour analyser le contenu HTML d'une page et extraire les données des questions ###
def parse_page(content): 
    if content is None: # Vérifie si le contenu est None, ce qui indique une erreur lors de la récupération de la page.
        return []

    soup = BeautifulSoup(content, 'html.parser') # Analyse le contenu HTML avec BeautifulSoup.
    questions_data = []
    questions = soup.find_all('div', id=lambda x: x and x.startswith('question-summary-'))

    for question in questions:
        title_element = question.find('h3')
        title = title_element.text.strip() if title_element else 'No title'
        link_element = question.find('a', class_='question-hyperlink')
        link = link_element['href'] if link_element else 'No link'
        summary_element = question.find('div', class_='s-post-summary--content-excerpt')
        summary = summary_element.text.strip() if summary_element else 'No summary'
        tags_elements = question.find_all('a', class_='post-tag')
        tags = [tag.text for tag in tags_elements]
        author_details = question.find('div', class_='s-user-card--link')
        author = author_details.a.text.strip() if author_details and author_details.a else 'Anonymous'
        date_element = question.find('span', class_='relativetime')
        date = date_element['title'] if date_element else 'No date'

        stats = question.find_all('div', class_='s-post-summary--stats-item')
        votes = stats[0].find('span', class_='s-post-summary--stats-item-number').text.strip() if len(stats) > 0 else '0'
        answers = stats[1].find('span', class_='s-post-summary--stats-item-number').text.strip() if len(stats) > 1 else '0'
        views = stats[2].find('span', class_='s-post-summary--stats-item-number').text.strip() if len(stats) > 2 else '0'

        questions_data.append({
            'title': title,
            'link': f"https://stackoverflow.com{link}",
            'summary': summary,
            'tags': tags,
            'author': author,
            'date': date,
            'votes': votes,
            'answers': answers,
            'views': views
        })

    return questions_data

### Fonction pour scraper les questions Stack Overflow en utilisant BeautifulSoup avec parallélisation pour améliorer la performance ###
def scrape_with_optimized_beautifulsoup(max_pages=100):
    base_url = "https://stackoverflow.com/questions?tab=newest&page="
    urls = [f"{base_url}{page}" for page in range(1, max_pages + 1)] # Liste des URLs pour chaque page à scraper, construite en fonction du nombre de pages spécifié

    all_data = []
    with ThreadPoolExecutor(max_workers=5) as executor: # Initialise un pool de threads avec un maximum de 5 threads pour exécuter les tâches en parallèle.
        future_to_url = {executor.submit(fetch_page, url): url for url in urls} # Soumet des tâches pour récupérer le contenu des pages à l'exécuteur et associe chaque future à son URL

        for future in as_completed(future_to_url): #  Itère sur les futurs qui sont complétés
            url = future_to_url[future]
            content = future.result() # Obtient le contenu de la page depuis le futur
            data = parse_page(content) # Analyse le contenu de la page et extrait les données
            all_data.extend(data) # Ajoute les données extraites à la liste all_data
    
    return all_data
