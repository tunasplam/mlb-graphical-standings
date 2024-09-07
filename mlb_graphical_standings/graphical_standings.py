# TODO what if its not baseball season? See README

# TODO clean up images somehow. put them into tmp when in docker?

import argparse

# TODO put dot back when building
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
