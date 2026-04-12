import requests
from bs4 import BeautifulSoup
import csv
import re

url = "https://www.ceneo.pl/Kremy_do_twarzy"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "pl-PL,pl;q=0.9",
}

# --- funkcje czyszczące ---


def clean_ocena(val):
    if not val:
        return None
    match = re.search(r"[\d,\.]+", val)
    return float(match.group().replace(",", ".")) if match else None


def clean_liczba(val):
    if not val:
        return None
    match = re.search(r"\d+", val)
    return int(match.group()) if match else None


# --- scraping ---

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

produkty = []

for row in soup.select("div.cat-prod-row"):
    name = row.select_one("strong.cat-prod-row__name span")
    score = row.select_one("span.product-score")
    reviews = row.select_one("span.prod-review__qo a")
    purchased = row.select_one("span.recently-purchased__level")

    produkty.append(
        {
            "nazwa": name.get_text(strip=True) if name else None,
            "ocena": clean_ocena(score.get_text(strip=True) if score else None),
            "recenzje": clean_liczba(reviews.get_text(strip=True) if reviews else None),
            "kupione_ostatnio": clean_liczba(
                purchased.get_text(strip=True) if purchased else None
            ),
        }
    )

# --- zapis do CSV ---

with open("wyniki.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(
        f, fieldnames=["nazwa", "ocena", "recenzje", "kupione_ostatnio"]
    )
    writer.writeheader()
    writer.writerows(produkty)

print(f"Zapisano {len(produkty)} produktów do wyniki.csv")
for p in produkty:
    print(p)
