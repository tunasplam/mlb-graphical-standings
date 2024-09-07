# MLB-GRAPHICAL-STANDINGS

# When it is not baseball season then this should email us some fairly hilarious content about it not being baseball season.

## Setup

[Use mailtrap.](https://api-docs.mailtrap.io/)

Put 'Domain Admin' token as `MAILTRAP_API_TOKEN`.

Set `TARGET_EMAIL` in `.env` file to be the email address you want to email these standings to.

Set `FROM_EMAIL` in `.env` to be the email address you want to send from.
We only want to send emails to ourself so just use `demomailtrap.com`. Otherwise, provide your own email in the `mailtrap.io` web ui.

Captions are generated using GPT model from openai. Create a new project there and generate an API key for it.

Pay $5 to set up a free paid account. Set monthly budget to $5.

Cost per run: entirely negligible.


## Usage

Build
```
chuy build
```

Test
```
chuy build test
```

## What to Expect

This will be a docker image. It will be loaded onto a Raspberry Pi and scheduled to run every Monday morning. It will load up graphical standings for each division, package them up, and then email them to me. Bonus if theres highlighted notes regarding lead changes!

What this will use

- pytest for testing
- Poetry to handle python deps
- docker to handle deployment

Roadmap

X setup basic grpahical standings

X fix clashing colors

X Make into an email

X would be really cool if we had chatgpt generate humorous captions

O test coverage

O docker 

O get logging setup once we have docker in place

