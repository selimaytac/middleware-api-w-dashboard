# app/services/rabbitmq_service.py

from sqlalchemy.orm import Session
from app.models.rabbitmq import RabbitMQInventory
from app.schemas.rabbitmq import RabbitMQCreate, RabbitMQUpdate

def get_rabbitmq(db: Session, rabbitmq_id: int):
    return db.query(RabbitMQInventory).filter(RabbitMQInventory.id == rabbitmq_id).first()

def get_rabbitmqs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RabbitMQInventory).order_by(RabbitMQInventory.hostname).offset(skip).limit(limit).all()

def create_rabbitmq(db: Session, rabbitmq: RabbitMQCreate):
    db_rabbitmq = RabbitMQInventory(**rabbitmq.dict())
    db.add(db_rabbitmq)
    db.commit()
    db.refresh(db_rabbitmq)
    return db_rabbitmq

def update_rabbitmq(db: Session, rabbitmq_id: int, rabbitmq: RabbitMQUpdate):
    db_rabbitmq = get_rabbitmq(db, rabbitmq_id)
    if not db_rabbitmq:
        return None
    for key, value in rabbitmq.dict().items():
        setattr(db_rabbitmq, key, value)
    db.commit()
    db.refresh(db_rabbitmq)
    return db_rabbitmq

def delete_rabbitmq(db: Session, rabbitmq_id: int):
    db_rabbitmq = get_rabbitmq(db, rabbitmq_id)
    if not db_rabbitmq:
        return None
    db.delete(db_rabbitmq)
    db.commit()
    return db_rabbitmq
