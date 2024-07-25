from scraping_scripts.scrapping import scrape_with_beautifulsoup, scrape_with_selenium
from scraping_scripts.optimized_scrapping import scrape_with_optimized_beautifulsoup
from scraping_scripts.api_scrapping import scrape_with_api
from bdd.database import save_to_mongo
import time

def main():
    print("Avec quelle méthode scraper le site ?")
    print("1. BeautifulSoup")
    print("2. Selenium")
    print("3. BeautifulSoup Optimisé")
    print("4. API Stack Overflow")
    
    method = input("Entrez le numéro de votre choix (1, 2, 3 ou 4): ").strip()
    
    while method not in ["1", "2", "3", "4"]:
        print("Choix invalide. Veuillez entrer '1' pour BeautifulSoup, '2' pour Selenium, '3' pour BeautifulSoup Optimisé ou '4' pour API Stack Overflow.")
        method = input("Entrez le numéro de votre choix (1, 2, 3 ou 4): ").strip()
    
    pages = input("Entrez le nombre de pages à scraper (default: 1 pour API, 100 pour les autres): ").strip()
    if not pages.isdigit():
        if method == "4":
            pages = 1
        else:
            pages = 100
    else:
        pages = int(pages)
    
    start_time = time.time()

    if method == "1":
        print("Scraping with BeautifulSoup...")
        data = scrape_with_beautifulsoup(max_pages=pages)
    elif method == "2":
        print("Scraping with Selenium...")
        data = scrape_with_selenium(max_pages=pages)
    elif method == "3":
        print("Scraping with Optimized BeautifulSoup...")
        data = scrape_with_optimized_beautifulsoup(max_pages=pages)
    elif method == "4":
        print("Scraping with API Stack Overflow...")
        data = scrape_with_api(max_pages=pages)
    
    if data:
        save_to_mongo(data)
        end_time = time.time()
        duration = end_time - start_time
        method_name = {
            "1": "BeautifulSoup",
            "2": "Selenium",
            "3": "Optimized BeautifulSoup",
            "4": "API Stack Overflow"
        }[method]
        print(f"Votre programme a scrapé {pages} pages en {duration:.2f} secondes avec la méthode {method_name}.")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
