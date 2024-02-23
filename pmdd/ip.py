from ipaddress import IPv4Address
import httpx


def get_ipv4() -> IPv4Address:
    return IPv4Address(httpx.get('https://ip.felixhummel.de/').text.strip())
