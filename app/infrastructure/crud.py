from sqlalchemy.orm import Session
from app.domain.models import Character
from app.domain.schemas import CharacterCreate

def get_character_by_id(db: Session, character_id: int):
    return db.query(Character).filter(Character.id == character_id).first()

def get_characters(db: Session):
    return db.query(Character).all()

def create_character(db: Session, character: CharacterCreate):
    db_character = Character(**character.dict())
    db.add(db_character)
    db.commit()
    db.refresh(db_character)
    return db_character

def delete_character(db: Session, character_id: int):
    db_character = db.query(Character).filter(Character.id == character_id).first()
    if db_character:
        db.delete(db_character)
        db.commit()
    return db_character
