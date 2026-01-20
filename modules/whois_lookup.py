# modules/whois_lookup.py

import whois
from datetime import datetime

def _format_date(value):
    """
    Normalize WHOIS date fields.
    """
    if isinstance(value, list):
        value = value[0]

    if isinstance(value, datetime):
        return value.strftime("%Y-%m-%d")

    return str(value) if value else "N/A"


def get_whois(domain: str) -> dict:
    """
    Perform WHOIS lookup for a domain.

    Args:
        domain (str): Target domain

    Returns:
        dict: Structured WHOIS information
    """

    result = {
        "domain": domain,
        "registrar": "N/A",
        "creation_date": "N/A",
        "expiration_date": "N/A",
        "name_servers": []
    }

    try:
        w = whois.whois(domain)

        result["registrar"] = w.registrar or "N/A"
        result["creation_date"] = _format_date(w.creation_date)
        result["expiration_date"] = _format_date(w.expiration_date)

        if w.name_servers:
            result["name_servers"] = [
                ns.lower() for ns in w.name_servers
            ]

    except Exception:
        # WHOIS failures are common; fail gracefully
        pass

    return result
