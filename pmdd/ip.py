from ipaddress import ip_address
import httpx


def get_ipv4() -> ip_address:
    return ip_address(httpx.get('https://ip.felixhummel.de/').text.strip())
