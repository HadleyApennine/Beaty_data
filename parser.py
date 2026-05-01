from utils import clean_liczba, clean_ocena


def parse_products(soup):
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
                "recenzje": clean_liczba(
                    reviews.get_text(strip=True) if reviews else None
                ),
                "kupione_ostatnio": clean_liczba(
                    purchased.get_text(strip=True) if purchased else None
                ),
            }
        )
    return produkty
