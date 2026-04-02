import requests
from bs4 import BeautifulSoup

url = "https://www.ceneo.pl/Kremy_do_twarzy"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9",
}

session = requests.Session()
session.get("https://www.ceneo.pl/", headers=headers)
response = session.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

# Szukamy wszystkich nazw produktów
produkty = soup.find_all("strong", class_="cat-prod-row__name")

for produkt in produkty:
    nazwa = produkt.find("span").text.strip()
    print(nazwa)
