# app/models/rabbitmq.py

from sqlalchemy import Column, Integer, String
from app.models.base import Base

class RabbitMQInventory(Base):
    __tablename__ = 'rabbitmq_inventory'

    id = Column(Integer, primary_key=True, index=True)
    istirak = Column(String)
    rabbit_name = Column(String)
    hostname = Column(String)
    host_ip = Column(String)
    rabbit_user = Column(String)
    rabbit_password = Column(String)
    server_user = Column(String)
    server_password = Column(String)
    rabbit_version = Column(String)
    erlang_version = Column(String)
    note = Column(String)
