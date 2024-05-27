import whois
import dns.resolver

def fetch_domain_info(domain):
    domain_info = whois.whois(domain)
    dns_info = dns.resolver.resolve(domain, 'A')
    ip_addresses = [ip.to_text() for ip in dns_info]
    
    return {'domain_info': domain_info, 'ip_addresses': ip_addresses}
