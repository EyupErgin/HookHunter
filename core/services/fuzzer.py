import string
import requests
import dns.resolver
from tqdm import tqdm
from fuzzywuzzy import fuzz
from tabulate import tabulate

class Fuzzer():
      
    def __init__(self, homoglyphs):
        self.homoglyphs = homoglyphs
        self.characters = string.ascii_lowercase + string.digits

    def check_availability(self, domain):
        try:
            response = requests.get("http://" + domain, timeout=5)  # HTTP isteği at
            return response.status_code, response.url  # HTTP durum kodunu ve URL'yi döndür
        except requests.RequestException as e:
            return "ERR", None  # HTTP isteği başarısızsa hata döndür

    def get_ip_address(self, domain):
        try:
            answers = dns.resolver.resolve(domain, 'A')  # A kaydı için IP adresini al
            for answer in answers:
                return answer.address
        except dns.resolver.NXDOMAIN:
            return "N/A"
        except dns.exception.Timeout:
            return "Timeout"
        except Exception as e:
            return "N/A"

    def add_character(self, domain):
        return [domain[:i] + c + domain[i:] for i in range(len(domain) + 1) for c in self.characters]

    def remove_character(self, domain):
        return [domain[:i] + domain[i+1:] for i in range(len(domain))]

    def replace_character(self, domain):
        return [domain[:i] + c + domain[i+1:] for i in range(len(domain)) for c in self.characters]

    def homoglyph_variations(self, domain):
        variations = []
        for i, char in enumerate(domain):
            for variant in self.homoglyphs.get(char, (char,)):
                new_domain = domain[:i] + variant + domain[i+1:]
                variations.append(new_domain)
        return variations

    def hyphenation(self, domain):
        return [domain[:i] + '-' + domain[i:] for i in range(1, len(domain))]

    def get_abuse_contact(self, domain):
        try:
            domain_info = whois.whois(domain)

            if domain_info.status is None or "No match for" in domain_info.status:
                return "N/A"

            if isinstance(domain_info.emails, list):
                valid_emails = [email.lower() for email in domain_info.emails if "@" in email]  # E-posta adreslerini küçük harfe çevir
                if not valid_emails:
                    return "N/A"

                abuse_emails = [email for email in valid_emails if "abuse" in email]
                if abuse_emails:
                    return abuse_emails[0]
                return min(valid_emails, key=len) if valid_emails else "N/A"
            elif isinstance(domain_info.emails, str):
                email = domain_info.emails.lower()  # E-posta adresini küçük harfe çevir
                return email if "abuse" in email and "@" in email else "N/A"
        except Exception as e:
            return "N/A"

    def generate_domain_variations(self, domain):
        domain_parts = domain.split('.')
        domain_name = domain_parts[0]
        tld = '.'.join(domain_parts[1:])

        data = []

        variations = []

        for variation in self.add_character(domain_name):
            variations.append(["CA", domain, variation + '.' + tld])

        for variation in self.remove_character(domain_name):
            variations.append(["CD", domain, variation + '.' + tld])

        for variation in self.replace_character(domain_name):
            variations.append(["CR", domain, variation + '.' + tld])

        for variation in self.homoglyph_variations(domain_name):
            variations.append(["HM", domain, variation + '.' + tld])

        for variation in self.hyphenation(domain_name):
            variations.append(["HP", domain, variation + '.' + tld])

        headers = ["#", "SC", "BASE DOMAIN", "IMPERSONATING DOMAIN", "SIMILARITY", "HTTP STATUS", "IP ADDRESS", "ABUSE E-MAIL"]

        pbar = tqdm(variations, unit=" domains", desc="Processing", ncols=100)

        idx = 0
        for variation in pbar:
            idx += 1
            similarity = fuzz.ratio(domain, variation[2])
            available, url = self.check_availability(variation[2])
            ip_address = self.get_ip_address(variation[2])
            abuse_email = self.get_abuse_contact(variation[2])

            if variation[2] != domain:
                data.append([idx, variation[0], variation[1], variation[2], similarity, available, ip_address, abuse_email])

        table = tabulate(data, headers, tablefmt="simple")
        print("\n")
        print(table)
