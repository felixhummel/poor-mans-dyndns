from pydantic import BaseModel


class Zone(BaseModel):
    id: str
    name: str

    @classmethod
    def from_json(cls, x):
        return cls(id=x['id'], name=x['name'])


RecordType = str


class Record(BaseModel):
    type: RecordType
    id: str
    name: str
    zone_id: str

    @classmethod
    def from_json(cls, x):
        return cls(
            id=x['id'],
            name=x['name'],
            type=x['type'],
            zone_id=x['zone_id'],
        )
