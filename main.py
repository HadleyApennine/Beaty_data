import csv
from scraper import get_soup
from parser import parse_products
import logging

soup = get_soup()
products = parse_products(soup)

with open("results.csv", "w", newline="", encoding="utf-8-sig") as f:
    writer = csv.DictWriter(
        f, fieldnames=["name", "rating", "reviews", "purchesed_recently"]
    )
    writer.writeheader()
    writer.writerows(products)

logging.basicConfig(
    filename="logs.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8",
)

logging.info(f"Saved {len(products)} products to results.csv")

print(f"Scraping finished, succesfully scraped {len(products)} items.")
