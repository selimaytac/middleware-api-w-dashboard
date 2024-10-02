# app/routers/rabbitmq.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import rabbitmq as schemas
from app.services import rabbitmq_service
from app.db.dependencies import get_db

router = APIRouter(
    prefix="/rabbitmq",
    tags=["RabbitMQ Inventory"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[schemas.RabbitMQ])
def read_rabbitmqs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    rabbitmqs = rabbitmq_service.get_rabbitmqs(db, skip=skip, limit=limit)
    return rabbitmqs

@router.post("/", response_model=schemas.RabbitMQ)
def create_rabbitmq(rabbitmq: schemas.RabbitMQCreate, db: Session = Depends(get_db)):
    return rabbitmq_service.create_rabbitmq(db=db, rabbitmq=rabbitmq)

@router.get("/{rabbitmq_id}", response_model=schemas.RabbitMQ)
def read_rabbitmq(rabbitmq_id: int, db: Session = Depends(get_db)):
    db_rabbitmq = rabbitmq_service.get_rabbitmq(db, rabbitmq_id=rabbitmq_id)
    if db_rabbitmq is None:
        raise HTTPException(status_code=404, detail="RabbitMQ entry not found")
    return db_rabbitmq

@router.put("/{rabbitmq_id}", response_model=schemas.RabbitMQ)
def update_rabbitmq(rabbitmq_id: int, rabbitmq: schemas.RabbitMQUpdate, db: Session = Depends(get_db)):
    db_rabbitmq = rabbitmq_service.update_rabbitmq(db=db, rabbitmq_id=rabbitmq_id, rabbitmq=rabbitmq)
    if db_rabbitmq is None:
        raise HTTPException(status_code=404, detail="RabbitMQ entry not found")
    return db_rabbitmq

@router.delete("/{rabbitmq_id}", response_model=schemas.RabbitMQ)
def delete_rabbitmq(rabbitmq_id: int, db: Session = Depends(get_db)):
    db_rabbitmq = rabbitmq_service.delete_rabbitmq(db=db, rabbitmq_id=rabbitmq_id)
    if db_rabbitmq is None:
        raise HTTPException(status_code=404, detail="RabbitMQ entry not found")
    return db_rabbitmq
