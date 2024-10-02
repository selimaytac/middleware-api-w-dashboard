# app/routers/elk.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import elk as schemas
from app.services import elk_service
from app.db.dependencies import get_db

router = APIRouter(
    prefix="/elk",
    tags=["ELK Inventory"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=list[schemas.ELK])
def read_elks(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    elks = elk_service.get_elks(db, skip=skip, limit=limit)
    return elks

@router.post("/", response_model=schemas.ELK)
def create_elk(elk: schemas.ELKCreate, db: Session = Depends(get_db)):
    return elk_service.create_elk(db=db, elk=elk)

@router.get("/{elk_id}", response_model=schemas.ELK)
def read_elk(elk_id: int, db: Session = Depends(get_db)):
    db_elk = elk_service.get_elk(db, elk_id=elk_id)
    if db_elk is None:
        raise HTTPException(status_code=404, detail="ELK entry not found")
    return db_elk

@router.put("/{elk_id}", response_model=schemas.ELK)
def update_elk(elk_id: int, elk: schemas.ELKUpdate, db: Session = Depends(get_db)):
    db_elk = elk_service.update_elk(db=db, elk_id=elk_id, elk=elk)
    if db_elk is None:
        raise HTTPException(status_code=404, detail="ELK entry not found")
    return db_elk

@router.delete("/{elk_id}", response_model=schemas.ELK)
def delete_elk(elk_id: int, db: Session = Depends(get_db)):
    db_elk = elk_service.delete_elk(db=db, elk_id=elk_id)
    if db_elk is None:
        raise HTTPException(status_code=404, detail="ELK entry not found")
    return db_elk
