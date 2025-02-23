"""
Everything regarding the creation of the charts goes here.
So pulling the data and creating and saving the charts.
"""

from io import BytesIO
from typing import List
import re
import warnings

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pybaseball as pb
from tqdm import tqdm

from .caption_generator import generate_caption
from .utils import get_soup, block_print, enable_print, COLORS_CACHE

warnings.simplefilter(action='ignore', category=FutureWarning)

URL_ROOT = "https://www.baseball-reference.com/"

def create_content(season: int, prompt: str) -> dict:
    """Create charts for each division in a given season. Saves them
    in memory. Then returns all of the info in dicts

    Returns (dict, dict): First dict is images stored in memory.
    Second is info on the division.
    """
    divisions = extract_divisions(season)

    for division, sd in divisions.items():
        print(division)
        division_gbs = calculate_division_gb(season, sd['teams'])
        sd['image'] = create_chart(division, sd['teams'], division_gbs)
        sd['caption'] = generate_caption(division_gbs, prompt)

    return divisions

def calculate_division_gb(season: int, teams: List[str]) -> pd.DataFrame:
    division_gbs = pd.DataFrame()

    block_print()
    for team in tqdm(teams):
        team_df = pb.schedule_and_record(season, team)
        team_df['GB'] = team_df['GB'].dropna().apply(modify_gb)
        division_gbs[team] = team_df['GB']

    enable_print()
    return division_gbs

def create_chart(division: str, teams: List[str], division_gbs: pd.DataFrame) -> BytesIO:
    ax = plt.axes()
    ax.figure.figsize = (8,6)

    for team in teams:
        # If we have a color for this team cached, then use it
        # otherwise have plt autoassign.
        if team in COLORS_CACHE:
            ax.plot(division_gbs[team], label=team, c=COLORS_CACHE[team])
        else:
            ax.plot(division_gbs[team], label=team)

    plt.title(re.sub('_', ' ', division))
    plt.xticks(np.arange(0, len(division_gbs.index), step=20))
    plt.yticks(np.arange(0, -30, step=-5))
    plt.xlabel('Games')
    plt.ylabel('Games Back')
    plt.legend(loc='lower left')

    # save to RAM and return the image
    img_bytes = BytesIO()
    plt.savefig(img_bytes, format="png")
    img_bytes.seek(0)
    plt.close()
    return img_bytes

def modify_gb(gb: str) -> float:
    """Converts GB column from human-readable text to usable floats.
    """
    match gb:
        case 'Tied':
            return 0.0
        case gb if 'up' in gb:
            return 0.0
        case _:
            return -float(gb)

def extract_divisions(season: int) -> dict:
    """Returns a dict where key is division and value list is abbreviations
    of teams in that division for the requested season

    Args:
        season (int): Year of desired season

    Returns:
        dict: key is division and value list is abbreviations
            of teams in that division for the requested season
    """
    url = f"{URL_ROOT}leagues/majors/{season}-standings.shtml"
    soup = get_soup(url)

    # there are six tables below, one for each division.
    # they are table tags with id="standings_[A-Z]"
    tables = soup.find_all('table', id=re.compile(r"standings_[A-Z]"))

    divisions = {}
    for t in tables:
        division = determine_division(t)
        divisions[division] = {}
        divisions[division]['teams'] = extract_teams_from_division_table(t)

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
    url = URL_ROOT + link
    soup = get_soup(url)
    t = soup.find('a', href=re.compile(r"/leagues/[A-Z]{2}/\d{4}.shtml")).text

    return t

def extract_teams_from_division_table(table: BeautifulSoup) -> List[str]:
    """Extract list of BRef abbreviated team names from divisions table.
    """
    teams = []
    ths = table.tbody.find_all('th')
    for th in ths:
        team = re.findall(r"(?<=teams/)[A-Z]{3}", th.a['href'])[0]
        teams.append(team)

    return teams
