from datetime import datetime, timezone
import socket

from core.argument_parser import parse_arguments
from core import logger
from core.report_writer import write_report

from modules.whois_lookup import get_whois
from modules.dns_enum import enumerate_dns
from modules.subdomain_enum import enumerate_subdomains
from modules.port_scan import scan_ports
from modules.banner_grab import grab_banners
from modules.tech_detect import detect_technologies


def resolve_target(domain: str):
    """
    Resolve domain to IP address
    """
    try:
        return socket.gethostbyname(domain)
    except socket.gaierror:
        logger.error("Failed to resolve target")
        return None


def main():
    args = parse_arguments()
    logger.set_verbose(args.verbose)

    logger.info(f"Starting reconnaissance on {args.target}")

    start_time = datetime.now(timezone.utc).isoformat()
    target_ip = resolve_target(args.target)

    if not target_ip:
        logger.error("Exiting due to resolution failure")
        return

    results = {
        "target": args.target,
        "ip_address": target_ip,
        "scan_start_time": start_time,
        "modules": {}
    }

    # WHOIS
    if args.whois:
        logger.info("Running WHOIS lookup")
        results["modules"]["whois"] = get_whois(args.target)

    # DNS Enumeration
    if args.dns:
        logger.info("Running DNS enumeration")
        results["modules"]["dns"] = enumerate_dns(args.target)

    # Subdomain Enumeration
    if args.subdomains:
        logger.info("Running subdomain enumeration (crt.sh)")
        results["modules"]["subdomains"] = enumerate_subdomains(args.target)

    # Port Scanning
    open_ports = []
    if args.ports:
        logger.info(f"Running socket-based port scan on ports: {args.ports}")
        open_ports = scan_ports(target_ip, args.ports)
        results["modules"]["open_ports"] = open_ports

    # Banner Grabbing (only if ports were scanned)
    if args.banners:
        if not open_ports:
            logger.warning("Banner grabbing requested but no ports were scanned")
        else:
            logger.info("Running banner grabbing")
            results["modules"]["banners"] = grab_banners(target_ip, open_ports)

    if args.tech:
        if not open_ports:
            logger.warning("Technology detection requires open ports")
        else:
            logger.info("Running technology detection")
            results["modules"]["technologies"] = detect_technologies(
                target_ip, open_ports
            )

    results["scan_end_time"] = datetime.now(timezone.utc).isoformat()

    report_path = write_report(args.target, results)
    logger.info(f"Report saved to {report_path}")


if __name__ == "__main__":
    main()
