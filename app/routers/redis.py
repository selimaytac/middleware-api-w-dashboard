from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import redis as schemas
from app.services import redis_service
from app.db.database import SessionLocal

router = APIRouter(prefix="/redis", tags=["Redis Inventory"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Redis])
def read_redises(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    redises = redis_service.get_redises(db, skip=skip, limit=limit)
    return redises

@router.post("/", response_model=schemas.Redis)
def create_redis(redis: schemas.RedisCreate, db: Session = Depends(get_db)):
    return redis_service.create_redis(db=db, redis=redis)

@router.get("/{redis_id}", response_model=schemas.Redis)
def read_redis(redis_id: int, db: Session = Depends(get_db)):
    db_redis = redis_service.get_redis(db, redis_id=redis_id)
    if db_redis is None:
        raise HTTPException(status_code=404, detail="Redis not found")
    return db_redis

@router.put("/{redis_id}", response_model=schemas.Redis)
def update_redis(redis_id: int, redis: schemas.RedisUpdate, db: Session = Depends(get_db)):
    return redis_service.update_redis(db=db, redis_id=redis_id, redis=redis)

@router.delete("/{redis_id}", response_model=schemas.Redis)
def delete_redis(redis_id: int, db: Session = Depends(get_db)):
    return redis_service.delete_redis(db=db, redis_id=redis_id)
