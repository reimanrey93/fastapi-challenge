from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.infrastructure.db.database import SessionLocal
from app.infrastructure import crud
from app.domain.schemas import CharacterCreate, CharacterResponse
from app.domain.models import Character  # Importa el modelo `Character`

router = APIRouter()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/character/getAll", response_model=list[CharacterResponse])
def get_all_characters(db: Session = Depends(get_db)):
    characters = crud.get_characters(db)
    return characters

@router.get("/character/get/{id}", response_model=CharacterResponse)
def get_character_by_id(id: int, db: Session = Depends(get_db)):
    character = crud.get_character_by_id(db, id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.post("/character/add", response_model=CharacterResponse)
def add_character(character: CharacterCreate, db: Session = Depends(get_db)):
    try:
        existing_character = db.query(Character).filter(Character.name == character.name).first()
        if existing_character:
            raise HTTPException(status_code=400, detail="Character already exists")
        return crud.create_character(db, character)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

@router.delete("/character/delete/{id}")
def delete_character(id: int, db: Session = Depends(get_db)):
    character = crud.delete_character(db, id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return {"detail": "Character deleted successfully"}
