from bs4 import BeautifulSoup
import requests

# declarer une url
url = "https://quotes.toscrape.com/"

# effectuer une requete sur l'URL
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text,"html.parser")

    quotes = soup.find_all("div",class_="quote")

    for quote in quotes:
        title = quote.find("span").text
        autor = quote.find("small").text
        tags = [tag.text for tag in quote.find_all("a",class_="tag")]

        print(f"{title} écrit {autor}")
        print(f"{' | '.join(tags)} \n")

else:
    print(f"Impossible d'effectuer la requete : {response.status_code}")



