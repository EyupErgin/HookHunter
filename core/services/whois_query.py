import whois

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