import string

def is_uppercase(inp):
    special_char = string.punctuation
    return inp.isupper() if inp not in special_char else True