import time

from bs4 import BeautifulSoup
import requests


def get_score(url: str):
    while not time.sleep(1):
        try:
            r = requests.get(url)
            soup = BeautifulSoup(r.content, "html.parser")
            return [
                el.contents[0]
                for el in soup.find_all("td", {"class": "R"})
            ]
        # If it hasn't been graded, soup.find_all() will return None
        except Exception:
            pass

