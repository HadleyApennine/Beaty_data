import csv
from scraper import get_soup
from parser import parse_products

soup = get_soup()
produkty = parse_products(soup)

with open("wyniki.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(
        f, fieldnames=["nazwa", "ocena", "recenzje", "kupione_ostatnio"]
    )
    writer.writeheader()
    writer.writerows(produkty)

print(f"Zapisano {len(produkty)} produktów do wyniki.csv")
