# modules/subdomain_enum.py

import requests

def enumerate_subdomains(domain: str) -> dict:
    """
    Enumerate subdomains using crt.sh (certificate transparency logs).

    Args:
        domain (str): Target domain

    Returns:
        dict: Subdomain enumeration results
    """

    subdomains = set()
    url = f"https://crt.sh/?q=%25.{domain}&output=json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return {
                "source": "crt.sh",
                "subdomains": []
            }

        data = response.json()

        for entry in data:
            name = entry.get("name_value", "")
            for sub in name.split("\n"):
                sub = sub.strip().lower()

                # Ignore wildcards
                if sub.startswith("*."):
                    sub = sub[2:]

                if sub.endswith(domain):
                    subdomains.add(sub)

    except Exception:
        # Network errors, JSON errors, etc.
        pass

    return {
        "source": "crt.sh",
        "subdomains": sorted(subdomains)
    }
