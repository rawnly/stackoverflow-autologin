import toml
from stackoverflow import StackOverflow
import os

config_path = "{folder}/config.toml".format(folder=os.path.dirname(os.path.abspath(__file__)))

if os.path.isfile(config_path):
    config = toml.load(config_path)
else:
    config = {
        "user": {
            "username": os.getenv("STACKOVERFLOW_USERNAME"),
            "password": os.getenv("STACKOVERFLOW_PASSWORD")
        },
        "notifications": {
            "webhook": os.getenv("WEBHOOK_URL")
        }
    }


# Create the connection 
connection = StackOverflow(config["user"]["username"], config["user"]["password"], config["notifications"]["webhook"])

# Login and check if the user is logged
connection.login()
isLogged = connection.logged()

# if logged print
# else display an error
if isLogged:
    print('StackOverflow: Logged')
else:
    print('StackOverflow: Can\'t login.. try again later.')

# close the session
connection.close()
