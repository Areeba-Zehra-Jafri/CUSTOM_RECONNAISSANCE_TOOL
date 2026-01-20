# modules/dns_enum.py

import dns.resolver

def enumerate_dns(domain: str) -> dict:
    """
    Perform DNS enumeration for A, MX, NS, and TXT records.

    Args:
        domain (str): Target domain

    Returns:
        dict: DNS records
    """

    records = {
        "A": [],
        "MX": [],
        "NS": [],
        "TXT": []
    }

    resolver = dns.resolver.Resolver()

    # A records (IPv4)
    try:
        answers = resolver.resolve(domain, "A")
        for rdata in answers:
            records["A"].append(rdata.to_text())
    except Exception:
        pass

    # MX records (mail servers)
    try:
        answers = resolver.resolve(domain, "MX")
        for rdata in answers:
            records["MX"].append(str(rdata.exchange).rstrip('.'))
    except Exception:
        pass

    # NS records (name servers)
    try:
        answers = resolver.resolve(domain, "NS")
        for rdata in answers:
            records["NS"].append(str(rdata.target).rstrip('.'))
    except Exception:
        pass

    # TXT records (SPF, verification, etc.)
    try:
        answers = resolver.resolve(domain, "TXT")
        for rdata in answers:
            txt_record = "".join(part.decode() for part in rdata.strings)
            records["TXT"].append(txt_record)
    except Exception:
        pass

    return records
