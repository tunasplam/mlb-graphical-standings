"""
This creates and sends the email.
"""

import base64
from datetime import datetime
from os import environ
import re
from typing import List

import mailtrap as mt

def send_offseason_email(content: str):
    client = mt.MailtrapClient(token=environ['MAILTRAP_API_TOKEN'])
    client.send(
        mt.Mail(
            sender=mt.Address(email=environ['FROM_EMAIL'], name="MLB Standings Bot"),
            to=[mt.Address(email=environ['TARGET_EMAIL'])],
            subject="MLB GRAPHICAL STANDINGS",
            text=content
        )
    )

def send_email(content: dict):
    client = mt.MailtrapClient(token=environ['MAILTRAP_API_TOKEN'])
    client.send(
        mt.Mail(
            sender=mt.Address(email=environ['FROM_EMAIL'], name="MLB Standings Bot"),
            to=[mt.Address(email=environ['TARGET_EMAIL'])],
            subject="MLB GRAPHICAL STANDINGS",
            html=format_html(content),
            attachments=prep_attachments(content)
        )
    )

def prep_attachments(content: dict) -> List[mt.Attachment]:
    return [
        mt.Attachment(
            content=base64.b64encode(sd['image'].getvalue()),
            filename=f"{division}.png",
            disposition=mt.Disposition.INLINE,
            mimetype="image/png",
            content_id=f"{division}.png"
        ) for division, sd in content.items()
    ]

def format_html(content: dict) -> str:
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

    for division in content:
        html += f"""
            <h1 style="font-size: 18px; font-weight: bold; margin-top: 20px">{re.sub(r'_', r' ', division)}</h1>
            <img alt="Cool Graph" src="cid:{division}.png" style="width: 100%;">
            <p>{content[division]['caption']}</p>"""

    html += """
        </div>
        <style>
            .main { background-color: white; }
            a:hover { border-left-width: 1em; min-height: 2em; }
        </style>
        </body>"""

    return html
