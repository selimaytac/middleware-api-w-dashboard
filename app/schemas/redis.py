from pydantic import BaseModel

class RedisBase(BaseModel):
    istirak: str
    name: str
    hostname: str
    host_ip: str
    lb_ip: str
    require_password: str
    server_user: str
    server_password: str
    version: str
    note: str

class RedisCreate(RedisBase):
    pass

class RedisUpdate(RedisBase):
    pass

class Redis(RedisBase):
    id: int

    class Config:
        orm_mode = True

class RedisResponse(RedisBase):
    id: int

    class Config:
        orm_mode = True
