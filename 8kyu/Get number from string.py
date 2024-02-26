def get_number_from_string(st):
    # Initialize an empty string to store digits
    digits = ''

    # Iterate through each character in the string
    for char in st:
        # Check if the character is a digit
        if char.isdigit():
            digits += char

    # Convert the accumulated digits to an integer
    result = int(digits)

    return result