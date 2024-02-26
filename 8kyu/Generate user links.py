from urllib.parse import quote

def generate_link(user):
    # Encode the username to make it URL-friendly
    encoded_username = quote(user)

    # Concatenate the parts of the URL
    link = f"http://www.codewars.com/users/{encoded_username}"

    return link