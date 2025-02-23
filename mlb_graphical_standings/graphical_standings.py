import argparse
from datetime import datetime

from .content_creation import create_content
from .email_formatter import send_email

def main():
    parser = argparse.ArgumentParser(
        prog='graphical_standings',
        description='sends you emails of mlb graphics.'
    )

    parser.add_argument(
        '-s','--season',
        action='store', type=int, nargs=1,
        default=datetime.now().year,
        help="Which season to choose. Defaults to current."
    )

    parser.add_argument(
        '-p', '--prompt',
        action='store', type=str, nargs=1,
        help="Path to prompt to use for ChatGPT-generated captions."
    )

    args = parser.parse_args()

    match args.season:
        case None:
            parser.print_help()
            exit(1)
        case _:
            if args.prompt is None:
                prompt = "Attached is information regarding the games behind of each team in an MLB division. Generate a caption that will be attached to lineplots displaying the trend of the games behind as time passes. Be completely whacko. Go crazy and have fun. Babble like a madman from the cartoon Adventure Time."
            else:
                with open(args.prompt, 'r', encoding='utf-8') as f:
                    prompt = f.read()

            content = create_content(args.season[0], prompt)
            send_email(content)

if __name__ == '__main__':
    main()
