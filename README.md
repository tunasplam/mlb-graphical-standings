# MLB-GRAPHICAL-STANDINGS

# When it is not baseball season then this should email us some fairly hilarious content about it not being baseball season.

## Setup

### Mailtrap account

This project uses Mailtrap to send the emails. You can use their smtp servers to send emails to yourself.

[Get an API token somewhere here](https://api-docs.mailtrap.io/)

Put 'Domain Admin' token as `MAILTRAP_API_TOKEN`.

Set `TARGET_EMAIL` in `.env` file to be your email address that you used to sign up for Mailtrap.

Set `FROM_EMAIL` in `.env` to be the email address you want to send from.
We only want to send emails to ourself so just use `demomailtrap.com`. Otherwise, provide your own email in the `mailtrap.io` web ui.

### OpenAI account

Captions are generated using GPT model from OpenAI. Create a new project there and generate an API key for it.

Set `OPENAI_API_KEY` in `.env` to be your OpenAI Project API key dedicated to this venture.

Pay $5 to set up a free paid account. Set monthly budget to $5.

Cost per run: entirely negligible.

### Usage

```
usage: graphical_standings [-h] [-s SEASON]

sends you emails of mlb graphics.

options:
  -h, --help            show this help message and exit
  -s SEASON, --season SEASON
```

### RaspberryPi
You can run this whereever you'd like, but I opted to do so on a Raspberry Pi.


## Developing

Build
```
chuy build
```

Test
```
chuy build test
```

## What to Expect

This program grabs current division standings in the MLB and creates a report with a captioned lineplot representing the progression of the season to date. It then emails the report to a myself.

Roadmap

X setup basic grpahical standings

X fix clashing colors

X Make into an email

X would be really cool if we had chatgpt generate humorous captions

Next:
    O clone this repo onto a Raspberry Pi
    O install poetry
    O configure everything to run
    O hook this up to cron
Document the entire installation procedure.

O test coverage

O get logging setup

