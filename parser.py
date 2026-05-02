from utils import clean_number, clean_rating


def parse_products(soup):
    products = []

    for row in soup.select("div.cat-prod-row"):
        name = row.select_one("strong.cat-prod-row__name span")
        score = row.select_one("span.product-score")
        reviews = row.select_one("span.prod-review__qo a")
        purchased = row.select_one("span.recently-purchased__level")

        products.append(
            {
                "name": name.get_text(strip=True) if name else None,
                "rating": clean_rating(score.get_text(strip=True) if score else None),
                "reviews": clean_number(
                    reviews.get_text(strip=True) if reviews else None
                ),
                "purchesed_recently": clean_number(
                    purchased.get_text(strip=True) if purchased else None
                ),
            }
        )
    return products
