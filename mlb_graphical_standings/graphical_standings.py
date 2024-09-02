from typing import List
import re
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import pybaseball as pb
from tqdm import tqdm

# TODO put dot back when building
from utils import get_soup, block_print, enable_print, COLORS_CACHE

URL_ROOT = "https://www.baseball-reference.com/"

def create_charts(season: int):
    """Create charts for each division in a given season. Saves them
    as pngs. Returns list of filepaths to these pngs.
    """

    #divisions = extract_divisions(season)
    divisions = {
        'AL_East': ['BAL', 'NYY', 'TOR', 'TBR', 'BOS'],
        'AL_Central': ['DET', 'KCR', 'CLE', 'CHW', 'MIN'],
        'AL_West': ['LAA', 'OAK', 'SEA', 'HOU', 'TEX'],
        'NL_East': ['WSN', 'ATL', 'NYM', 'MIA', 'PHI'],
        'NL_Central': ['STL', 'PIT', 'MIL', 'CIN', 'CHC'],
        'NL_West': ['LAD', 'SFG', 'SDP', 'COL', 'ARI']
    }

    return [create_chart(season, division, divisions[division]) for division in divisions]

def create_chart(season: int, division: str, teams: List[str]) -> str:
    """Create standings chart for given season/division. Saves the chart
    to disk and returns the filepath.

    Args:
        season (int): year of desired season
        division (str): division to generate standings for
        teams (List[str]): list of teams from that division

    Returns:
        str: path to saved chart
    """
    ax = plt.axes()
    ax.figure.figsize = (8,6)

    print(f"Getting schedule and records for {division}")
    num_games = 0
    block_print()
    for team in tqdm(teams):
        team_df = pb.schedule_and_record(season, team)

        # set how many games have been played so that xticks can adapt
        if num_games == 0:
            num_games = len(team_df.index)

        team_df['GB'] = team_df['GB'].dropna().apply(modify_gb)

        # If we have a color for this team cached, then use it
        # otherwise have plt autoassign.
        if team in COLORS_CACHE:
            ax.plot(team_df['GB'], label=team, c=COLORS_CACHE[team])
        else:
            ax.plot(team_df['GB'], label=team)

        # TODO setting team logo shields at the end would be cool
        # shield = plt.imread(f"../resources/{team}.png")
        # ax.figure.figimage(shield, team_df.loc[num_games, 'GB'], num_games)

    enable_print()

    plt.title(re.sub('_', ' ', division))
    plt.xticks(np.arange(0, num_games, step=20))
    plt.yticks(np.arange(0, -30, step=-5))
    plt.xlabel('Games')
    plt.ylabel('Games Back')
    plt.legend(loc='lower left')

    # TODO better filepath handling
    fname = f'{division}.png'
    plt.savefig(fname)
    plt.clf()
    return fname

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
    url = URL_ROOT + link
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

create_charts(2014)
