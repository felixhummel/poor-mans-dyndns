import os

from ipaddress import IPv4Address
import httpx


URL = os.environ.get('PMDD_IP_URL', 'https://ip.hetzner.com/')


def get_ipv4() -> IPv4Address:
    return IPv4Address(httpx.get('https://ip.felixhummel.de/').text.strip())
