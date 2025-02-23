# MLB-GRAPHICAL-STANDINGS

## Setup

### Mailtrap account

This project uses Mailtrap to send the emails. You can use their smtp servers to send emails to yourself.

[Get an API token somewhere here](https://api-docs.mailtrap.io/)

Create a `.env` in `~/.config/mlb-graphical-standings` using `.env.sample`

Put 'Domain Admin' token as `MAILTRAP_API_TOKEN`.

Set `TARGET_EMAIL` in `.env` file to be your email address that you used to sign up for Mailtrap.

Set `FROM_EMAIL` in `.env` to be the email address you want to send from.
We only want to send emails to ourself so just use `demo@demomailtrap.com`. Otherwise, provide your own email in the `mailtrap.io` web ui.

### OpenAI account

Captions are generated using GPT model from OpenAI. Create a new project there and generate an API key for it.

Set `OPENAI_API_KEY` in `.env` to be your OpenAI Project API key dedicated to this venture.

Pay $5 to set up a free paid account. Set monthly budget to $5.

Cost per run: entirely negligible.

### Usage

```
usage: graphical_standings [-h] [-s SEASON] [-p PROMPT]

sends you emails of mlb graphics.

options:
  -h, --help            show this help message and exit
  -s SEASON, --season SEASON
                        Which season to choose. Defaults to current. Older seasons may not work.
  -p PROMPT, --prompt PROMPT
                        Path to prompt to use for ChatGPT-generated captions.
```

Here is the default prompt:

    Attached is information regarding the games behind of each team in an MLB division.Generate a caption that will be attached to lineplots displaying the trend of the games behind as time passes. Be completely whacko. Go crazy and have fun. Babble like a madman from the cartoon Adventure Time.

If you don't like it, then you can change it by specifying the path to a .txt
file containing the desired prompt. I recommend putting it in `~/.config/mlb-graphical-standings/prompt.txt`. You can even have multiple prompts and have some script choose one at random. Just have fun with it.

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

O test coverage

O When it is not baseball season it should send us fairly hilarious content about it not being baseball season.