import socket
from core import logger

# Common probes for banner grabbing
PROBES = {
    80: b"HEAD / HTTP/1.0\r\n\r\n",
    443: b"HEAD / HTTP/1.0\r\n\r\n",
    21: b"\r\n",     # FTP
    22: b"\r\n",     # SSH
    25: b"HELO test\r\n",  # SMTP
}


def grab_banner(target_ip: str, port: int, timeout: float = 2.0):
    """
    Grab banner from a single port using sockets
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((target_ip, port))

        # Send probe if known service
        probe = PROBES.get(port, b"\r\n")
        sock.sendall(probe)

        banner = sock.recv(1024).decode(errors="ignore").strip()
        sock.close()

        if banner:
            return banner

    except Exception as e:
        logger.debug(f"Banner grab failed on port {port}: {e}")

    return None


def grab_banners(target_ip: str, open_ports: list):
    """
    Grab banners from multiple open ports
    """
    banners = {}

    for port in open_ports:
        logger.debug(f"Grabbing banner from port {port}")
        banner = grab_banner(target_ip, port)

        if banner:
            banners[port] = banner

    return banners
