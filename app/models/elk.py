# app/models/elk.py

from sqlalchemy import Column, Integer, String
from app.models.base import Base

class ELKInventory(Base):
    __tablename__ = 'elk_inventory'

    id = Column(Integer, primary_key=True, index=True)
    istirak = Column(String)
    name = Column(String)
    hostname = Column(String)
    host_ip = Column(String)
    lb_ip = Column(String)
    elastic_url = Column(String)
    kibana_url = Column(String)
    elastic_user = Column(String)
    elastic_password = Column(String)
    server_user = Column(String)
    server_password = Column(String)
    version = Column(String)
    note = Column(String)
