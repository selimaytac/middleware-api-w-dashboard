from sqlalchemy import Column, Integer, String
from app.models.base import Base

class RedisInventory(Base):
    __tablename__ = 'redis_inventory'
    
    id = Column(Integer, primary_key=True, index=True)
    istirak = Column(String)
    name = Column(String)
    hostname = Column(String)
    host_ip = Column(String)
    lb_ip = Column(String)
    require_password = Column(String)
    server_user = Column(String)
    server_password = Column(String)
    version = Column(String)
    note = Column(String)
