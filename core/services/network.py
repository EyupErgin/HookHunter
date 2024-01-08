import requests
import dns.resolver

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