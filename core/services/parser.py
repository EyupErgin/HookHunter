from urllib.parse import urlparse

def parse_domain(user_input):
    parsed_url = urlparse(user_input)
    return parsed_url.netloc if parsed_url.netloc else user_input