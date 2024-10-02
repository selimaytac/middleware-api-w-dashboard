# app/schemas/elk.py

from pydantic import BaseModel

class ELKBase(BaseModel):
    istirak: str
    name: str
    hostname: str
    host_ip: str
    lb_ip: str
    elastic_url: str
    kibana_url: str
    elastic_user: str
    elastic_password: str
    server_user: str
    server_password: str
    version: str
    note: str

class ELKCreate(ELKBase):
    pass

class ELKUpdate(ELKBase):
    pass

class ELK(ELKBase):
    id: int

    class Config:
        orm_mode = True

class ELKResponse(ELKBase):
    id: int

    class Config:
        orm_mode = True
