from sqlalchemy.orm import Session
from app.models.redis import RedisInventory
from app.schemas.redis import RedisCreate, RedisUpdate

def get_redis(db: Session, redis_id: int):
    return db.query(RedisInventory).filter(RedisInventory.id == redis_id).first()

def get_redises(db: Session, skip: int = 0, limit: int = 100):
    return db.query(RedisInventory).order_by(RedisInventory.hostname).offset(skip).limit(limit).all()

def create_redis(db: Session, redis: RedisCreate):
    db_redis = RedisInventory(**redis.dict())
    db.add(db_redis)
    db.commit()
    db.refresh(db_redis)
    return db_redis

def update_redis(db: Session, redis_id: int, redis: RedisUpdate):
    db_redis = get_redis(db, redis_id)
    for key, value in redis.dict().items():
        setattr(db_redis, key, value)
    db.commit()
    db.refresh(db_redis)
    return db_redis

def delete_redis(db: Session, redis_id: int):
    db_redis = get_redis(db, redis_id)
    db.delete(db_redis)
    db.commit()
    return db_redis
