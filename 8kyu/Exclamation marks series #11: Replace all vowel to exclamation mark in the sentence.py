def replace_exclamation(st):
    vowels = "aeiouAEIOU"
    result = ""

    for char in st:
        if char in vowels:
            result += "!"
        else:
            result += char

    return result