from typing import List
import re

from bs4 import BeautifulSoup
import pybaseball as pb
from tqdm import tqdm

from .utils import get_soup

url_root = "https://www.baseball-reference.com/"

def extract_divisions(season: int) -> dict:
    """Returns a dict where key is division and value list is abbreviations
    of teams in that division for the requested season

    Args:
        season (int): Year of desired season

    Returns:
        dict: key is division and value list is abbreviations
            of teams in that division for the requested season
    """

    url = f"{url_root}leagues/majors/{season}-standings.shtml"
    soup = get_soup(url)

    # there are six tables below, one for each division.
    # they are table tags with id="standings_[A-Z]"
    tables = soup.find_all('table', id=re.compile(r"standings_[A-Z]"))

    divisions = {}
    print("Extracting divisions from BRef")
    for t in tqdm(tables):
        divisions[determine_division(t)] = extract_teams_from_division_table(t)

    return divisions

def determine_division(table: BeautifulSoup) -> str:
    """Given a standings table for a given season, extract the division name.
    This is done by navigating to the team page for that season from the first
    team listed on the table and extracting it from there.

    Args:
        table (BeautifulSoup): Season standings for division in season.

    Returns:
        str: Name of division
    """
    link = table.tbody.find_all('th')[0].a['href']
    url = url_root + link
    soup = get_soup(url)
    t = soup.find('a', href=re.compile(r"/leagues/[A-Z]{2}/\d{4}.shtml")).text

    return t

def extract_teams_from_division_table(table: BeautifulSoup) -> List[str]:

    teams = []
    ths = table.tbody.find_all('th')
    for th in ths:
        team = re.findall(r"(?<=teams/)[A-Z]{3}", th.a['href'])[0]
        teams.append(team)

    return teams
