"""
This creates and sends the email.
"""

from datetime import datetime
from os import environ
import re

from dotenv import load_dotenv
import mailtrap as mt

# TODO configure place for config file
load_dotenv('/home/jordan/mlb-graphical-standings/.env')

def send_email(divisions: dict):

    html = format_html(divisions)

    # create mail object
    # TODO send the custom html content
    mail = mt.Mail(
        sender=mt.Address(email=environ['FROM_EMAIL'], name="MLB Standings Bot"),
        to=[mt.Address(email=environ['TARGET_EMAIL'])],
        subject="MLB GRAPHICAL STANDINGS",
        text="Test email."
    )

    client = mt.MailtrapClient(token=environ['MAILTRAP_API_TOKEN'])
    client.send(mail)


def format_html(divisions: dict) -> str:
    """Takes info regarding divisions and formats the email HTML content.
    """

    date = datetime.strftime(datetime.now(), "%A %B %d, %Y")

    html = f"""
    <!doctype html>
    <html>
        <head>
            <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        </head>
        <body style="font-family: tahoma;">
        <div style="display: block; margin: auto; max-width: 600px;" class="main">
            <h1 style="font-size: 18px; font-weight: bold; margin-top: 20px">MLB Graphical Standings {date}</h1>
            <p>Have fun</p>"""

    for division in divisions:
        caption = 'Insert caption text here.'
        html += f"""
            <h1 style="font-size: 18px; font-weight: bold; margin-top: 20px">{re.sub(r'_', r' ', division)}</h1>
            <p>{caption}</p>
            <img alt="Cool Graph" src="{division}.png" style="width: 100%;">"""
        
    html += """
        </div>
        <style>
            .main { background-color: white; }
            a:hover { border-left-width: 1em; min-height: 2em; }
        </style>
        </body>"""

    print(html)

    return html

format_html({
        'AL_East': ['BAL', 'NYY', 'TOR', 'TBR', 'BOS'],
        'AL_Central': ['DET', 'KCR', 'CLE', 'CHW', 'MIN'],
        'AL_West': ['LAA', 'OAK', 'SEA', 'HOU', 'TEX'],
        'NL_East': ['WSN', 'ATL', 'NYM', 'MIA', 'PHI'],
        'NL_Central': ['STL', 'PIT', 'MIL', 'CIN', 'CHC'],
        'NL_West': ['LAD', 'SFG', 'SDP', 'COL', 'ARI']
    })