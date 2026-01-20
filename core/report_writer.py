import os
from datetime import datetime


def write_report(target: str, results: dict):
    """
    Write formatted recon report to a text file
    """
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)

    report_path = os.path.join(report_dir, f"{target}_{timestamp}.txt")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("Recon Report\n")
        f.write(f"Target: {target}\n")
        f.write(f"Timestamp: {timestamp}\n\n")

        f.write("=== TARGET ===\n")
        f.write(f"{results.get('target')}\n\n")

        f.write("=== IP ADDRESS ===\n")
        f.write(f"{results.get('ip_address')}\n\n")

        f.write("=== SCAN START TIME ===\n")
        f.write(f"{results.get('scan_start_time')}\n\n")

        modules = results.get("modules", {})

        # WHOIS
        if "whois" in modules:
            whois_data = modules["whois"]
            f.write("=== WHOIS ===\n")

            f.write(f"Domain: {whois_data.get('domain', 'N/A')}\n")
            f.write(f"Registrar: {whois_data.get('registrar', 'N/A')}\n")
            f.write(f"Creation Date: {whois_data.get('creation_date', 'N/A')}\n")
            f.write(f"Expiration Date: {whois_data.get('expiration_date', 'N/A')}\n")

            name_servers = whois_data.get("name_servers", [])
            if name_servers:
                f.write("Name Servers:\n")
                for ns in name_servers:
                    f.write(f"  - {ns}\n")
            else:
                f.write("Name Servers: N/A\n")

            f.write("\n")


        # DNS
        if "dns" in modules:
            f.write("=== DNS RECORDS ===\n")
            for record_type, values in modules["dns"].items():
                f.write(f"{record_type}:\n")
                for v in values:
                    f.write(f"  - {v}\n")
            f.write("\n")

        # Subdomains
        if "subdomains" in modules:
            f.write("=== SUBDOMAINS ===\n")
            for sub in modules["subdomains"]:
                f.write(f"- {sub}\n")
            f.write("\n")

        # Open Ports
        if "open_ports" in modules:
            f.write("=== OPEN PORTS ===\n")
            for port in modules["open_ports"]:
                f.write(f"{port}\n")
            f.write("\n")

        # Banners
        if "banners" in modules:
            f.write("=== BANNERS ===\n")
            if not modules["banners"]:
                f.write("No banners detected\n\n")
            else:
                for port, banner in modules["banners"].items():
                    f.write(f"[Port {port}]\n")
                    f.write(banner + "\n\n")

        # Technologies
        if "technologies" in modules:
            f.write("=== TECHNOLOGIES ===\n")
            if not modules["technologies"]:
                f.write("No technologies detected\n\n")
            else:
                for port, tech in modules["technologies"].items():
                    f.write(f"[Port {port}]\n")
                    for key, value in tech.items():
                        if isinstance(value, list):
                            f.write(f"{key}:\n")
                            for item in value:
                                f.write(f"  - {item}\n")
                        else:
                            f.write(f"{key}: {value}\n")
                    f.write("\n")

        f.write("=== SCAN END TIME ===\n")
        f.write(results.get("scan_end_time") + "\n")

    return report_path
