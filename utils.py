import re


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
