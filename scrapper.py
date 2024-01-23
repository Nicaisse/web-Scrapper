import requests
from bs4 import BeautifulSoup
import csv


def scraper(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        articles_container = soup.find("div", class_="lnv-featured-article")

        if articles_container:
            
            articles = articles_container.find_all(
                "div", class_="lnv-featured-article-sm"
            )

            for article in articles:
                title = article.find("h1").text.strip()
                link = article.find("a")["href"].strip()
                image = article.find("img")["src"].strip()
                description = article.find("p").text.strip()

                with open("data.csv", "a", newline="") as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([title, link, image, description])
        else:
            print("conteneur vide")
    else:
        print("erreur connexion")


scraper("https://lenouvelliste.com/")
