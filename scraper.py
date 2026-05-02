import requests
import logging
from bs4 import BeautifulSoup
from config import url, headers


def get_soup():
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

    except requests.exceptions.ConnectionError:
        logging.error("Internet not working.")
    except requests.exceptions.Timeout:
        logging.error("Server not responding.")
    except requests.exceptions.HTTPError as e:
        logging.error(f"HTTP Error: {e}")
