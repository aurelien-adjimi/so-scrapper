from scrapping import scrape_with_beautifulsoup, scrape_with_selenium
from optimized_scrapping import scrape_with_optimized_beautifulsoup
from api_scrapping import scrape_with_api
from database import save_to_mongo

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
        print("Scraping completed and data saved.")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
