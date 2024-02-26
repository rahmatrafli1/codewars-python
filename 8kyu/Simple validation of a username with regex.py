import re

def validate_usr(username):
    #your code here
    pattern = re.compile(r'^[a-z0-9_]{4,16}$')
    return bool(pattern.match(username))