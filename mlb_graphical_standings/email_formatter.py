"""
This creates and sends the email.
"""

import base64
from datetime import datetime
from dotenv import load_dotenv
from os import environ
from pathlib import Path
import re
from typing import List

import mailtrap as mt

# TODO configure place for config file
load_dotenv('/home/jordan/mlb-graphical-standings/.env')

def send_email(divisions: dict):

    client = mt.MailtrapClient(token=environ['MAILTRAP_API_TOKEN'])
    client.send(
        mt.Mail(
            sender=mt.Address(email=environ['FROM_EMAIL'], name="MLB Standings Bot"),
            to=[mt.Address(email=environ['TARGET_EMAIL'])],
            subject="MLB GRAPHICAL STANDINGS",
            html=format_html(divisions),
            attachments=prep_attachments(divisions)
        ),
    )

def prep_attachments(divisions: dict) -> List[mt.Attachment]:
    ats = []
    for division in divisions:
        division_img = Path(__file__).parent.joinpath(f"{division}.png").read_bytes()
        ats.append(
            mt.Attachment(
                # SMTH LIKE THIS
                content=base64.b64encode(division_img),
                filename=f"{division}.png",
                disposition=mt.Disposition.INLINE,
                mimetype="image/png",
                content_id=f"{division}.png"
            )
        )

    return ats

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
        html += f"""
            <h1 style="font-size: 18px; font-weight: bold; margin-top: 20px">{re.sub(r'_', r' ', division)}</h1>
            <img alt="Cool Graph" src="cid:{division}.png" style="width: 100%;">
            <p>{divisions[division]['caption']}</p>"""

    html += """
        </div>
        <style>
            .main { background-color: white; }
            a:hover { border-left-width: 1em; min-height: 2em; }
        </style>
        </body>"""

    print(html)

    return html
