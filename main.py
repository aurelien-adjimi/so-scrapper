from scrapping import scrape_with_beautifulsoup, scrape_with_selenium
from database import save_to_mongo

def main():
    print("Avec quelle librairie scraper le site ?")
    print("1. BeautifulSoup")
    print("2. Selenium")
    
    method = input("Entrez le numéro de votre choix (1 ou 2): ").strip()
    
    while method not in ["1", "2"]:
        print("Choix invalide. Veuillez entrer '1' pour BeautifulSoup ou '2' pour Selenium.")
        method = input("Entrez le numéro de votre choix (1 ou 2): ").strip()
    
    pages = input("Entrez le nombre de pages à scraper (default: 100): ").strip()
    if not pages.isdigit():
        pages = 100
    else:
        pages = int(pages)

    if method == "1":
        print("Scraping with BeautifulSoup...")
        data = scrape_with_beautifulsoup(max_pages=pages)
    elif method == "2":
        print("Scraping with Selenium...")
        data = scrape_with_selenium(max_pages=pages)

    if data:
        save_to_mongo(data)
        print("Scraping completed and data saved.")
    else:
        print("No data scraped.")

if __name__ == '__main__':
    main()
