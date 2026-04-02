import requests

headers = {
    "User-Agent": "Mozilla/5.0",
}

session = requests.Session()
r1 = session.get("https://www.douglas.pl/pl", headers=headers)
print(f"Status: {r1.status_code}")
print(r1.text[:500])
