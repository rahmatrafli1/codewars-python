def is_digit(n):
    #your code here
    # Check if the string is not None and consists of a single character which is a digit
    return n is not None and len(n) == 1 and n.isdigit()