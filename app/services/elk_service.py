# app/services/elk_service.py

from sqlalchemy.orm import Session
from app.models.elk import ELKInventory
from app.schemas.elk import ELKCreate, ELKUpdate

def get_elk(db: Session, elk_id: int):
    return db.query(ELKInventory).filter(ELKInventory.id == elk_id).first()

def get_elks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ELKInventory).order_by(ELKInventory.hostname).offset(skip).limit(limit).all()

def get_elks_without_password(db: Session, skip: int = 0, limit: int = 100)

def create_elk(db: Session, elk: ELKCreate):
    db_elk = ELKInventory(**elk.dict())
    db.add(db_elk)
    db.commit()
    db.refresh(db_elk)
    return db_elk

def update_elk(db: Session, elk_id: int, elk: ELKUpdate):
    db_elk = get_elk(db, elk_id)
    if not db_elk:
        return None
    for key, value in elk.dict().items():
        setattr(db_elk, key, value)
    db.commit()
    db.refresh(db_elk)
    return db_elk

def delete_elk(db: Session, elk_id: int):
    db_elk = get_elk(db, elk_id)
    if not db_elk:
        return None
    db.delete(db_elk)
    db.commit()
    return db_elk
