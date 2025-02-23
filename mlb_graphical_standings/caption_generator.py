"""Anything regarding using GPT to generate captions is done here.
"""
from os import environ
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

# check if config file exists and load
status = load_dotenv(Path(environ['HOME']) / Path('.config/mlb-graphical-standings/.env'))
if not status:
    raise RuntimeError('No config file found. Make sure you have a .env file in ~/.config/mlb-graphical-standings. Check the README!')

client = OpenAI()

def generate_caption(df: pd.DataFrame, prompt: str) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a cool and smart friend who thoroughly enjoys baseball. No emojis and no hashtags. Be professional but witty."
            },
            {
                "role": "user",
                "content": f"{prompt} Data: {str(df)}"
            }
        ]
    )

    return response.choices[0].message.content

def generate_offseason_content() -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "It is the baseball offseason and you are a bored reddit baseball fan creating content regarding baseball."
            },
            {
                "role": "user",
                "content": "It is the baseball offseason. Life is mundane and colorless. Please generate some fairly hilarious offseason content (make it \"peak\" content).)"
            }
        ]
    )

    return response.choices[0].message.content
