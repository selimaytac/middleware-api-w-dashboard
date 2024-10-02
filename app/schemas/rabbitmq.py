# app/schemas/rabbitmq.py

from pydantic import BaseModel

class RabbitMQBase(BaseModel):
    istirak: str
    rabbit_name: str
    hostname: str
    host_ip: str
    rabbit_user: str
    rabbit_password: str
    server_user: str
    server_password: str
    rabbit_version: str
    erlang_version: str
    note: str

class RabbitMQCreate(RabbitMQBase):
    pass

class RabbitMQUpdate(RabbitMQBase):
    pass

class RabbitMQ(RabbitMQBase):
    id: int

    class Config:
        orm_mode = True

class RabbitMQResponse(RabbitMQBase):
    id: int

    class Config:
        orm_mode = True