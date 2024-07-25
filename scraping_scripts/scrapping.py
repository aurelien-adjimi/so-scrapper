### Imports ###
import requests
from bs4 import BeautifulSoup
import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


### Fonction pour scraper le site avec BeautifulSoup ###
def scrape_with_beautifulsoup(max_pages=100):
    base_url = "https://stackoverflow.com/questions" # Je renseigne ici l'URL de base pour les pages de questions
    questions_data = [] # J'initialise une liste vide qui va stocker les données extraites

    for page in range(1, max_pages + 1): # Début de la boucle qui va parcourir les pages spécifiées
        url = f"{base_url}?tab=newest&page={page}" # Construction de l'URL pour chaque page
        response = requests.get(url) # Requête HTTP pour obtenir le contenu de la page

        if response.status_code == 200: # Vérification du code de retour de la requête
            soup = BeautifulSoup(response.text, 'html.parser') # J'analyse le contenu HTML de la page
            questions = soup.find_all('div', id=lambda x: x and x.startswith('question-summary-')) # Trouve toutes les div avec les informations des questions

            for question in questions: # Boucle qui va chercher tout le contenu de chaque question par le HTML et extrait ces informations
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

                stats = question.find_all('div', class_ = 's-post-summary--stats-item')
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

            time.sleep(1) # Ici je fais une pause afin d'éviter la surcharge du serveur
        else:
            print(f"Failed to retrieve the page {page}. Status code: {response.status_code}")
            break

    return questions_data

### Fonction pour scraper le site avec Selenium ###
def scrape_with_selenium(max_pages=100):
    questions_data = [] # J'initialise une liste vide qui va stocker les données extraites
    base_url = "https://stackoverflow.com/questions?tab=newest&page=" # Je renseigne ici l'URL de base pour les pages de questions

    chrome_options = webdriver.ChromeOptions() # Configure les options pour Chrome.
    chrome_options.add_argument("--headless") # Le mode headless permet d'exécuter en arrière-plan
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options) # Initialise le navigateur Chrome avec les options spécifiées.

    for page in range(1, max_pages + 1): # Début de la boucle qui va parcourir les pages spécifiées
        url = f"{base_url}{page}" # Construction de l'URL pour chaque page
        print(f"Scraping page {page} with Selenium...")
        driver.get(url) # Je charge la page avec Selenium.
        
        try:
            WebDriverWait(driver, 10).until( # Permet d'attendre que les éléments de la page soient présents avant de continuer.
                EC.presence_of_element_located((By.CSS_SELECTOR, 'div[id^="question-summary-"]'))
            )
        except Exception as e:
            print(f"Error loading page {page}: {e}")
            continue

        questions = driver.find_elements(By.CSS_SELECTOR, 'div[id^="question-summary-"]') # Trouve tous les éléments contenant les informations des questions.
        # print(f"Found {len(questions)} questions on page {page}")

        for question in questions: # # Boucle qui va chercher tout le contenu de chaque question par les classes et le HTML et extrait ces informations
            try:
                title_element = question.find_element(By.CSS_SELECTOR, 'h3.s-post-summary--content-title a.s-link')
                title = title_element.text.strip()
                link = title_element.get_attribute('href')
                summary_element = question.find_element(By.CSS_SELECTOR, '.s-post-summary--content-excerpt')
                summary = summary_element.text.strip() if summary_element else 'No summary'
                tags_elements = question.find_elements(By.CSS_SELECTOR, '.post-tag')
                tags = [tag.text for tag in tags_elements]
                author_element = question.find_element(By.CSS_SELECTOR, '.s-user-card--link a')
                author = author_element.text.strip() if author_element else 'Anonymous'
                date_element = question.find_element(By.CSS_SELECTOR, 'time')
                date = date_element.get_attribute('datetime') if date_element else 'No date'

                stats = question.find_elements(By.CSS_SELECTOR, '.s-post-summary--stats-item')
                votes = stats[0].find_element(By.CSS_SELECTOR, '.s-post-summary--stats-item-number').text.strip() if len(stats) > 0 else '0'
                answers = stats[1].find_element(By.CSS_SELECTOR, '.s-post-summary--stats-item-number').text.strip() if len(stats) > 1 else '0'
                views = stats[2].find_element(By.CSS_SELECTOR, '.s-post-summary--stats-item-number').text.strip() if len(stats) > 2 else '0'

                question_data = { # Ajoute les données de chaque question à la liste
                    'title': title,
                    'link': link,
                    'summary': summary,
                    'tags': tags,
                    'author': author,
                    'date': date,
                    'votes': votes,
                    'answers': answers,
                    'views': views
                }
                # print(f"Scraped question: {question_data}")
                questions_data.append(question_data)
            except Exception as e:
                print(f"Error processing question: {e}")

    driver.quit() # Ferme le navigateur une fois que toutes les pages ont été traitées.
    return questions_data
