import logging
import os

import click

from .ip import get_ipv4
from .porcellain import HetznerDNS

LOG_LEVELS = ['CRITICAL', 'FATAL', 'ERROR', 'WARN', 'WARNING', 'INFO', 'DEBUG']

logging.basicConfig()
log = logging.getLogger()
dns = HetznerDNS.from_environ()


@click.group
@click.option('-l', '--log-level',
              type=click.Choice(LOG_LEVELS, case_sensitive=False),
              default='WARNING')
def root(log_level):
    log.setLevel(log_level)


@root.command
def ip():
    print(get_ipv4())


@root.command
def zones():
    print(dns.zones())


@root.command
@click.option('--zone-id', envvar='PMDD_ZONE_ID')
def records(zone_id):
    print(dns.records(zone_id))


@root.group
def set():
    pass


@set.command
@click.option('--zone-id', envvar='PMDD_ZONE_ID')
@click.option('--name', envvar='PMDD_NAME')
def a_record(zone_id, name):
    if zone_id is None:
        raise ValueError('zone_id missing')
    if name is None:
        raise ValueError('name missing')
    ip = get_ipv4()
    dns.update(zone_id, name, str(ip))
