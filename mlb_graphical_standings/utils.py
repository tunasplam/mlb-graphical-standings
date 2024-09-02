from bs4 import BeautifulSoup
from pybaseball.datasources.bref import BRefSession

# this is a nice Session in pb that automatically spaces
# out requests to avoid bans.
session = BRefSession()

def get_soup(url: str) -> BeautifulSoup:
    s = session.get(url).content
    return BeautifulSoup(s, "lxml")
