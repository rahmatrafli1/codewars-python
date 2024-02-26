def validate(username, password):
    # Check for injected code in username or password
    if '||' in username or '//' in username or '||' in password or '//' in password:
        return "Wrong username or password!"

    # Assume the correct login logic here
    # For demonstration purposes, I'm using a simple check for the password 'password'
    if username == 'Timmy' and password == 'password':
        return "Successfully Logged in!"
    elif username == 'Alice' and password == 'alice':
        return "Successfully Logged in!"
    elif username == 'Admin' and password == 'ads78adsg7dasga':
        return "Successfully Logged in!"
    elif username == 'Johny' and password == 'Hf7FAbf6':
        return "Successfully Logged in!"
    elif username == 'Roger' and password == 'pass':
        return "Successfully Logged in!"
    elif username == 'Simon' and password == 'says':
        return "Successfully Logged in!"
    else:
        return "Wrong username or password!"
