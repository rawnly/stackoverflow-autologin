import toml
from stackoverflow import StackOverflow

with open("./config.toml", mode="r") as config_file:
    config = toml.load(config_file)

# Create the connection 
connection = StackOverflow(config["user"]["email"], configp["user"]["password"], config["notifications"]["webhook"])

# Login and check if the user is logged
connection.login()
isLogged = connection.logged()

# if logged print
# else display an error
if isLogged:
    print 'StackOverflow: Logged'
else:
    print 'StackOverflow: Can\'t login.. try again later.'

# close the session
connection.close()
