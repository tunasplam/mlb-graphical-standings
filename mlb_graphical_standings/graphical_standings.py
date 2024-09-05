# TODO what if its not baseball season?

# TODO extensive clean ups once this is all working

# TODO put dot back when building
from chart_creation import create_charts
from email_formatter import send_email

# TODO argparse stuff will go here
def main():
    divisions = create_charts(2014)
    send_email(divisions)


# TODO ditch when building
main()
