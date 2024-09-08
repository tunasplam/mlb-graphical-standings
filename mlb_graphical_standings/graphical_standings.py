# TODO what if its not baseball season? See README

# TODO clean up images somehow. put them into tmp when in rpi?

import argparse
from dotenv import load_dotenv
from os import environ
from pathlib import Path

# check if config file exists and load
status = load_dotenv(Path(environ['HOME']) / Path('.config/mlb-graphical-standings/.env'))
if not status:
    raise RuntimeException('No config file found. Make sure you have a .env file in ~/.config/mlb-graphical-standings. Check the README!')

from chart_creation import create_charts
from email_formatter import send_email

def main():
    parser = argparse.ArgumentParser(
        prog='graphical_standings',
        description='sends you emails of mlb graphics.'
    )

    parser.add_argument(
        '-s','--season',
        action='store', type=int, nargs=1
    )

    args = parser.parse_args()

    match args.season:
        case None:
            parser.print_help()
            exit(1)
        case _:
            send_email(create_charts(args.season[0]))

if __name__ == '__main__':
    main()
