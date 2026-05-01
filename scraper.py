import requests
from bs4 import BeautifulSoup
from config import url, headers


def get_soup():
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    return soup
