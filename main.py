from core.services.fuzzer import Fuzzer
from core.services.input import get_user_input
from core.services.parser import parse_domain
from urllib.parse import urlparse
import json

def main():
    print("""
______  __           ______ ______  __             _____               | Version: v1.0
___  / / /______________  /____  / / /___  __________  /_____________  | Developed by Eyup Sukru ERGIN
__  /_/ /_  __ \  __ \_  //_/_  /_/ /_  / / /_  __ \  __/  _ \_  ___/  | --------------------------------------
_  __  / / /_/ / /_/ /  ,<  _  __  / / /_/ /_  / / / /_ /  __/  /      | https://ergin.dev
/_/ /_/  \____/\____//_/|_| /_/ /_/  \__,_/ /_/ /_/\__/ \___//_/       | https://github.com/eyupergin/hookhunter

Advanced Domain Based Phishing and Impersonating Domain Detection Tool
""")

    with open("data/homoglyph/model.json", 'r') as file:
        homoglyphs = json.load(file)

    fuzzer = Fuzzer(homoglyphs)
    
    user_input = get_user_input()

    domain = parse_domain(user_input)

    fuzzer.generate_domain_variations(domain)

if __name__ == "__main__":
    main()