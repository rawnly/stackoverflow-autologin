import os
import toml
from typing import TypedDict

from stackoverflow import StackOverflow, Credentials
from stackoverflow.notification_manager import TwilioConfig, WebHooksConfig, NotificationManager


class Config(TypedDict):
    twilio: TwilioConfig
    webhooks: WebHooksConfig
    credentials: Credentials

FOLDER = os.path.dirname(
    os.path.abspath(__file__)
)

CONFIG_FILE = os.environ.get("CONFIG_FILE") or "config.toml"
CONFIG_PATH = f"{FOLDER}/{CONFIG_FILE}"

config: Config

if os.path.isfile(CONFIG_PATH):
    print(f"'{CONFIG_FILE}' found! Reading credentials from file.")

    toml_data = toml.load(CONFIG_PATH)

    config: Config = Config(
        twilio={
            'sid': toml_data["twilio"]["sid"],
            'token': toml_data["twilio"]["token"],
            'sender': toml_data["twilio"]["sender"],
            'to': toml_data["twilio"]["to"]
        },
        webhooks={
            'discord': toml_data["webhooks"]["discord"]
        },
        credentials={
            'username': toml_data["credentials"]["username"],
            'password': toml_data["credentials"]["password"]
        }
    )
else:
    print("No config file found. Reading credentials from ENV.")
    config: Config = Config(
        twilio={
            'sid': os.getenv("TWILIO_ACCOUNT_SID"),
            'token': os.getenv("TWILIO_AUTH_TOKEN"),
            'sender': os.getenv("TWILIO_SENDER"),
            'to': os.getenv("PHONE_NUMBER")
        },
        webhooks={
            'discord': os.getenv("DISCORD_WEBHOOK_URL")
        },
        credentials={
            'username': os.getenv("STACKOVERFLOW_USERNAME"),
            'password': os.getenv("STACKOVERFLOW_PASSWORD")
        }
    )

# Create the connection
connection: StackOverflow = StackOverflow(
    config['credentials']
)


notifier: NotificationManager = NotificationManager(
    twilio_config=config['twilio'],
    webhooks=config['webhooks']
)

# Login and check if the user is logged
connection.login()
isLogged = connection.logged()

# if logged print
# else display an error
if isLogged:
    msg = 'Successfully logged in!'

    print(msg)
    notifier.notify_discord(msg)
    notifier.notify_sms(msg)

else:
    msg = 'Can\'t login.. Please doublecheck your credentials and try again later.'

    print(msg)
    notifier.notify_discord(msg)
    notifier.notify_sms(msg)


# close the session
connection.close()
