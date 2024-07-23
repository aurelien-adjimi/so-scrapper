### Imports ###
import requests
from bdd.database import save_to_mongo

### Fonction qui envoie une requête à l'API Stack Exchange pour obtenir les questions ###
def fetch_questions_from_api(page=1, pagesize=100):
    url = f"https://api.stackexchange.com/2.3/questions"
    params = { # Définition des paramètres pour la récupération
        'order': 'desc',
        'sort': 'activity',
        'site': 'stackoverflow',
        'page': page,
        'pagesize': pagesize
    }
    
    response = requests.get(url, params=params) # Envoie la requête à l'API avec les paramètres spécifiés.
    response.raise_for_status() # Je vérifie la réponse
    data = response.json() # J'analyse la donnée, en convertissant la réponse en JSON. La fonction retourne la liste des questions contenues dans data['items'].
    return data['items']

### Fonction pour transformer les données des questions obtenues de l'API en un format structuré ###
### La fonction prend la liste des questions et extrait les informations pertinentes pour chaque question ###
def parse_question_data(questions):
    parsed_data = []
    for question in questions:
        parsed_data.append({
            'title': question.get('title', 'No title'),
            'link': question.get('link', 'No link'),
            'summary': question.get('body', 'No summary'),
            'tags': question.get('tags', []),
            'author': question.get('owner', {}).get('display_name', 'Anonymous'),
            'date': question.get('creation_date', 'No date'),
            'votes': question.get('score', '0'),
            'answers': question.get('is_answered', '0'),
            'views': question.get('view_count', '0')
        })
    return parsed_data

### Fonction pour gérer le processus complet de récupération et d'analyse des questions via l'API ###
def scrape_with_api(max_pages=1, pagesize=100):
    all_data = []
    for page in range(1, max_pages + 1): # Boucle pour récupérer les questions et les analyser et ajouter les résultats à la liste 
        print(f"Fetching page {page} from API...")
        questions = fetch_questions_from_api(page=page, pagesize=pagesize)
        data = parse_question_data(questions)
        all_data.extend(data)
    
    return all_data

if __name__ == "__main__":
    data = scrape_with_api(max_pages=2)
    save_to_mongo(data)
    print("API scraping completed and data saved.")
