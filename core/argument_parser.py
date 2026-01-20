# core/argument_parser.py

import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Custom Reconnaissance Tool"
    )

    parser.add_argument(
        "target",
        help="Target domain (e.g. example.com)"
    )

    parser.add_argument(
        "--whois",
        action="store_true",
        help="Perform WHOIS lookup"
    )

    parser.add_argument(
        "--dns",
        action="store_true",
        help="Perform DNS enumeration"
    )

    parser.add_argument(
        "--subdomains",
        action="store_true",
        help="Enumerate subdomains"
    )

    parser.add_argument(
        "--ports",
        help="Port range to scan (e.g. 1-1024 or 80,443,8080)",
        type=str
    )

    parser.add_argument(
        "--banners",
        action="store_true",
        help="Grab service banners from open ports (requires --ports)"
    )

    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )

    parser.add_argument(
    "--tech",
    action="store_true",
    help="Detect web technologies using HTTP headers (requires --ports)"
    )

    return parser.parse_args()
