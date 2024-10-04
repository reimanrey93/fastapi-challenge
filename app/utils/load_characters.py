from sqlalchemy.orm import Session
from app.infrastructure.db.database import SessionLocal
from app.infrastructure import crud
from app.domain.schemas import CharacterCreate

characters_to_load = [
    {
        "name": "Luke Skywalker",
        "height": 172,
        "mass": 77,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 19
    },
    {
        "name": "Darth Vader",
        "height": 202,
        "mass": 136,
        "hair_color": "none",
        "skin_color": "white",
        "eye_color": "yellow",
        "birth_year": 42  # Convertido a entero
    },
    {
        "name": "Leia Organa",
        "height": 150,
        "mass": 49,
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "birth_year": 19
    },
    {
        "name": "Obi-Wan Kenobi",
        "height": 182,
        "mass": 77,
        "hair_color": "auburn",
        "skin_color": "fair",
        "eye_color": "blue-gray",
        "birth_year": 57
    },
    {
        "name": "Yoda",
        "height": 66,
        "mass": 17,
        "hair_color": "white",
        "skin_color": "green",
        "eye_color": "brown",
        "birth_year": 896
    },
    {
        "name": "Han Solo",
        "height": 180,
        "mass": 80,
        "hair_color": "brown",
        "skin_color": "fair",
        "eye_color": "brown",
        "birth_year": 29
    },
    {
        "name": "Chewbacca",
        "height": 228,
        "mass": 112,
        "hair_color": "brown",
        "skin_color": "unknown",
        "eye_color": "blue",
        "birth_year": 200
    },
    {
        "name": "R2-D2",
        "height": 96,
        "mass": 32,
        "hair_color": "none",
        "skin_color": "white, blue",
        "eye_color": "red",
        "birth_year": 33
    },
    {
        "name": "C-3PO",
        "height": 167,
        "mass": 75,
        "hair_color": "none",
        "skin_color": "gold",
        "eye_color": "yellow",
        "birth_year": 112
    },
    {
        "name": "Boba Fett",
        "height": 183,
        "mass": 78,
        "hair_color": "black",
        "skin_color": "fair",
        "eye_color": "brown",
        "birth_year": 32
    }
]


def load_characters_to_db(db: Session):
    for character_data in characters_to_load:
        character = CharacterCreate(**character_data)
        existing_character = db.query(crud.Character).filter(crud.Character.name == character.name).first()
        
        if existing_character:
            print(f"Character {character.name} already exists, skipping.")
            continue
        
        crud.create_character(db, character)
        print(f"Character {character.name} added to the database.")

def main():
    db = SessionLocal()
    try:
        load_characters_to_db(db)
    finally:
        db.close()

if __name__ == "__main__":
    main()
