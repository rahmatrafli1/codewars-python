def hello(name=''):
    if name:
        # Capitalize the first letter and convert the rest to lowercase
        formatted_name = name.capitalize()
        return f"Hello, {formatted_name}!"
    else:
        return "Hello, World!"