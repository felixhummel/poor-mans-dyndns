from .models import Zone, Record
from .plumbing import HetznerDNSAPI


class HetznerDNS:
    def __init__(self, api: HetznerDNSAPI):
        self.api = api

    @classmethod
    def from_environ(cls):
        return cls(HetznerDNSAPI.from_environ())

    def zones(self):
        return [
            Zone.from_json(zone)
            for zone in self.api.list_zones()['zones']
        ]

    def records(self, zone_id):
        return [
            Record.from_json(rec)
            for rec in self.api.get_records(zone_id)['records']
        ]

    def get_a_record(self, zone_id, name):
        records = self.records(zone_id)
        for rec in records:
            if rec.type == 'A' and rec.name == name:
                return rec
        return None

    def update(self, zone_id, name, ip):
        # https://dns.hetzner.com/api-docs#operation/CreateRecord
        existing = self.get_a_record(zone_id, name)
        if existing is None:
            return self.api.create_record(zone_id, name, ip)
        else:
            return self.api.update_record(existing, name, ip)
