# modules/tech_detect.py

import socket
from core import logger


HTTP_PORTS = [80, 8080, 8000, 443]


def detect_http_tech(target_ip: str, port: int, timeout: float = 2.0):
    """
    Detect technologies via HTTP response headers
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((target_ip, port))

        request = b"HEAD / HTTP/1.1\r\nHost: target\r\n\r\n"
        sock.sendall(request)

        response = sock.recv(4096).decode(errors="ignore")
        sock.close()

        headers = {}

        for line in response.split("\r\n"):
            if ":" in line:
                key, value = line.split(":", 1)
                headers[key.strip()] = value.strip()

        tech = {
            "server": headers.get("Server"),
            "powered_by": headers.get("X-Powered-By"),
            "framework": headers.get("X-Framework"),
            "security_headers": [
                h for h in headers.keys()
                if h.lower().startswith("x-")
            ]
        }

        # Remove empty values
        return {k: v for k, v in tech.items() if v}

    except Exception as e:
        logger.debug(f"Tech detection failed on port {port}: {e}")

    return None


def detect_technologies(target_ip: str, open_ports: list):
    """
    Run tech detection on relevant HTTP ports
    """
    technologies = {}

    for port in open_ports:
        if port in HTTP_PORTS:
            logger.debug(f"Detecting technologies on port {port}")
            tech = detect_http_tech(target_ip, port)

            if tech:
                technologies[port] = tech

    return technologies
