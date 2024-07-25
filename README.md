# Projet de scraping de StackOverflow (so-scrapper)  
___  

## Contexte du projet  

Le web scraping est une technique permettant d'extraire automatiquement des données contenues dans des sites internet en utilisant des programmes informatiques. Cette méthode est très utilisée pour collecter des informations en grande quantité rapidement, ce qui s'avère utile dans des domaines tels que l'analyse de données et le marketing digital. Le web scraping pose toutefois des défis éthiques et légaux, nécessitant le respect des directives et des lois sur la protection des données.  


## Fonctionnalités requises  
1. Extraction de données de Stack Overflow:  
- Titres des questions
- Liens vers les questions  
- Résumés des questions
- Tags associés aux questions
- Détails des auteurs 
- Date de publication
- Statistiques des questions

2. Stockage des données extraites:  
- Stockage structuré dans une base de données non relationnelle (MongoDB)  

3. Analyse des données:  
- Identifier des tendances dans les technologies, les langages de programmation ou autres tags pertinents (utilisation de techniques de NLP possible)  

4. Tests Unitaires:  
- Gestion des requêtes HTTP
- Analyse du HTML
- Extraction des données
- Insertion des données dans la BDD  

5. Parallélisation:  
- Utilisation de techniques de parallélisation pour accélérer le processus de collecte des données.  

6. Utilisation de l'API Stack Overflow:  
- Extraction de données plus fiable et respectueuse des règles du site, en complément ou en remplacement du scraping direct.  

## Architecture du projet

so-scrapper/  
│  
├── bdd/  
│   └── database.py  
│  
├── scraping_scripts/  
│   ├── scrapping.py  
│   ├── optimized_scrapping.py  
│   └── api_scrapping.py  
│  
├── test/  
│   ├── test_data_extract.py  
│   ├── test_html.py  
│   ├── test_insert.py  
│   └── test_request.py  
│  
├── scrap-env/  
│  
├── .gitattributes  
├── .gitignore  
├── main.py  
├── requirements.txt  
├── scrap-notebook.ipynb  
└── README.md  

## Utilisation de l'outil

1. Configuration de l'environnement virtuel  
- Exécutez la commande `python -m venv scrap-env`
- Activez l'environnement avec les commandes `cd scrap-env/Scripts` puis `.\activate`  

2. Installez les dépendances  
- Exécutez la commande `pip install -r requirements.txt`  

3. Lancez le script principal  
- Exécutez la commande `python main.py`  

4. Choisissez la méthode de scraping  
- 1 = Scraping avec BeautifulSoup  
- 2 = Scraping avec Selenium
- 3 = Scraping avec BeautifulSoup optimisé
- 4 = Scraping via l'API StackExchange  

Dans le terminal tapez votre choix  

5. Choisissez le nombre de pages à scraper  
- Tapez dans le terminal un nombre entre 1 et 100 (qui est le nombre de page par défaut)  

6. Visualisez les données  
- Dans le notebook 'scrap-notebook.ipynb' vous retrouverez plusieurs visualisations de donnée.

## Tests Unitaires
### Objectifs des Tests  
Les tests unitaires sont essentiels pour garantir le bon fonctionnement de chaque composant du projet. Ils permettent de s'assurer que le code fonctionne comme prévu et facilitent la maintenance du projet en détectant rapidement les régressions.  

### Description des Tests  
- test_request.py:
    - Objectif: Vérifier la gestion des requêtes HTTP.
    - Description: Utilise 'unittest.mock' pour simuler des requêtes HTTP et vérifier que le code traite correctement les réponses.

- test_html.py:
    - Objectif: Tester l'analyse du HTML
    - Description: Vérifie que le parser HTML peut extraire les éléments nécessaires d'une page HTML statique.

- test_data_extract.py:
    - Objectif: Vérifier l'extraction des données
    - Description: Simule une page HTML de Stack Overflow et s'assure que les données sont correctement extraites et formatées.

- test_insert.py:
    - Objectif: Tester l'insertion des données dans la base de données MongoDB.
    - Description: Utilise 'unittest.mock' pour simuler l'insertion de données et s'assure que les données sont bien insérées dans la collection MongoDB.


### Exécution des Tests
Pour exécuter les Tests utilisez la commande `pytest` ou, pour exécuter les tests un par un `python nom_du_fichier_test.py`.
