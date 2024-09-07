"""Anything regarding using GPT to generate captions is done here.
"""
from dotenv import load_dotenv
from openai import OpenAI
import pandas as pd

# TODO configure place for config file
load_dotenv('/home/jordan/mlb-graphical-standings/.env')

client = OpenAI()

def generate_caption(df: pd.DataFrame) -> str:

    with open('prompt.txt', 'r') as f:
        prompt = f.read()

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
