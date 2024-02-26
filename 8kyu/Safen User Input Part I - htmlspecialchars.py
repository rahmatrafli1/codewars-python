def html_special_chars(data): 
    # your code here
    html_entities = {
        "&": "&amp;",
        "<": "&lt;",
        ">": "&gt;",
        '"': "&quot;"
    }

    return ''.join(html_entities.get(char, char) for char in data)