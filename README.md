# StackOverflow Login
> A simple script to login into StackOverflow

## Why 
When I started this little project the objective was reaching the "Enthusiast" badge on [StackOverflow][stack]
> Visit the site each day for 30 consecutive days. (Days are counted in UTC.)

It's just a simple web-scraper built on top of [`requests`][requests] and `beautifulsoup4`

## How to use
```sh
  pip install -r requirements.txt
```

Right know the scraper supports custom notifications via Twilio and Discord.

You can setup the environment using ENV variables, names are pretty self explanatory:

- **STACKOVERFLOW_USERNAME** 
- **STACKOVERFLOW_PASSWORD**
- PHONE_NUMBER
- TWILIO_ACCOUNT_SID
- TWILIO_AUTH_TOKEN
- TWILIO_SENDER
- DISCORD_WEBHOOK_URL

<small>NOTE: **BOLD** variables are required.</small>

Otherwise if you're running it locally you can setup a config  `toml` file. Filename can be customised via the env variable `CONFIG_FILE`.

To run the script just execute the `main.py`

## Suggestion
I suggest to run a CI Job every day at the same hour. (Look at the [workflows](.github/workflows))

[requests]: http://docs.python-requests.org/en/master/
[stack]: https://stackoverflow.com/
