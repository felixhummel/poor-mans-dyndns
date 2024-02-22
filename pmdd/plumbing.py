import logging
import os

import httpx

from .models import Record


log = logging.getLogger(__package__)


class HetznerDNSAPI:
    """
    plumbing
    """
    URL = 'https://dns.hetzner.com/api/v1'
    TTL = 60

    def __init__(self, client: httpx.Client):
        self.client = client

    @classmethod
    def from_token(cls, token):
        headers = {'Auth-API-Token': token}
        client = httpx.Client(
                headers=headers,
                base_url=cls.URL,
        )
        return cls(client)

    @classmethod
    def from_environ(cls):
        token = os.environ['HETZNER_DNS_TOKEN']
        return cls.from_token(token)

    def list_zones(self):
        # https://dns.hetzner.com/api-docs#operation/GetZones
        return self.client.get('/zones').json()

    def get_records(self, zone_id):
        # https://dns.hetzner.com/api-docs#operation/GetRecords
        return self.client.get(f'/records?zone_id={zone_id}').json()

    def request(self, method, path, payload):
        log.debug(method)
        log.debug(path)
        log.debug(payload)
        try:
            response = self.client.request(method, path, json=payload)
            response.raise_for_status()
            return response
        except httpx.HTTPError as e:
            log.error(response.text)
            raise

    def post(self, path, payload):
        return self.request('POST', path, payload)

    def put(self, path, payload):
        return self.request('PUT', path, payload)

    def create_record(self, zone_id, name, ip):
        # https://dns.hetzner.com/api-docs#operation/UpdateRecord
        return self.post('/records', {
            'zone_id': zone_id,
            'type': 'A',
            'name': name,
            'value': ip,
            'ttl': self.TTL,
        })

    def update_record(self, record: Record, name, ip):
        record_id = record.id
        path = f'/records/{record_id}'
        return self.put(path, {
            'zone_id': record.zone_id,
            'type': 'A',
            'name': record.name,
            'value': ip,
            'ttl': self.TTL,
        })

if __name__ == '__main__':
    api = HetznerDNSAPI.from_environ()
    print(str(api.list_zones()))
