import socket
from core import logger


def parse_ports(port_input: str):
    """
    Parse port input:
    - 1-1024
    - 80,443,8080
    """
    ports = set()

    try:
        if "-" in port_input:
            start, end = port_input.split("-")
            ports.update(range(int(start), int(end) + 1))
        else:
            for p in port_input.split(","):
                ports.add(int(p.strip()))

    except ValueError:
        logger.error("Invalid port format")
        return []

    return sorted(ports)


def scan_ports(target_ip: str, port_input: str, timeout: float = 1.0):
    """
    Perform TCP connect scan using sockets
    """
    open_ports = []
    ports = parse_ports(port_input)

    logger.debug(f"Parsed ports: {ports}")

    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((target_ip, port))
            sock.close()

            if result == 0:
                logger.info(f"Port {port} is OPEN")
                open_ports.append(port)

        except Exception as e:
            logger.debug(f"Error scanning port {port}: {e}")

    return open_ports
