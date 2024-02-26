def remove(s):
    # Check if the string ends with an exclamation mark
    if s.endswith('!'):
        # Remove the last character
        return s[:-1]
    else:
        # If no exclamation mark at the end, return the original string
        return s