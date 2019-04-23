from login import StackOverflow

# Create the connection
connection = StackOverflow("fedevitale99@gmail.com", "Fagocero99")

# Login and check if the user is logged
connection.login()
isLogged = connection.logged()


if isLogged:
    print 'Welcome @%s! \nStackOverflow login successfully done.' % connection.USER["nick"]
else:
    print 'Sorry can\'t login.. try again later.\nMaybe you have 2FA enabled or StackOverflow is blocking scrapers'

# close the session
connection.close()
