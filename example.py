from login import StackOverflow

# Create the connection 
connection = StackOverflow("your_email_address", "your_password")

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
