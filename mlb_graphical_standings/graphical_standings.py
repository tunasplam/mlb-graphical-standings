# TODO what if its not baseball season?

# TODO extensive code clean ups once this is all working

# TODO clean up images somehow. in fact all filepaths for everything
# needs to be done better.


# TODO put dot back when building
from chart_creation import create_charts
from email_formatter import send_email

# TODO argparse stuff will go here
def main():
    divisions = create_charts(2024)
    send_email(divisions)

# TODO ditch when building
main()
