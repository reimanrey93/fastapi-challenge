import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.api.main import app
from app.infrastructure.db.database import Base, get_db

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

# Dependency override para pruebas
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

############### UNIT TESTS #####################################

#GETALL

def test_get_all_characters_empty():
    response = client.get("/character/getAll")
    assert response.status_code == 200
    assert response.json() == []

def test_get_all_characters_with_data():
    character_data = {
        "name": "Luke Skywalker",
        "height": 172,
        "mass": 77,
        "hair_color": "blond",
        "skin_color": "fair",
        "eye_color": "blue",
        "birth_year": 19
    }
    client.post("/character/add", json=character_data)
    
    response = client.get("/character/getAll")
    assert response.status_code == 200
    assert len(response.json()) > 0

#GET{ID}

def test_get_character_by_id():
    character_data = {
        "name": "Darth Vader",
        "height": 202,
        "mass": 136,
        "hair_color": "none",
        "skin_color": "white",
        "eye_color": "yellow",
        "birth_year": 42
    }
    response = client.post("/character/add", json=character_data)
    character_id = response.json()["id"]
    
    response = client.get(f"/character/get/{character_id}")
    assert response.status_code == 200
    assert response.json()["name"] == "Darth Vader"

def test_get_character_by_id_not_found():
    response = client.get("/character/get/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Character not found"}

#ADD

def test_add_character_success():
    character_data = {
        "name": "Leia Organa",
        "height": 150,
        "mass": 49,
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "birth_year": 19
    }
    response = client.post("/character/add", json=character_data)
    assert response.status_code == 200
    assert response.json()["name"] == "Leia Organa"

def test_add_character_duplicate():
    character_data = {
        "name": "Leia Organa",
        "height": 150,
        "mass": 49,
        "hair_color": "brown",
        "skin_color": "light",
        "eye_color": "brown",
        "birth_year": 19
    }
    response = client.post("/character/add", json=character_data)
    assert response.status_code == 400
    assert response.json() == {"detail": "Character already exists"}

#DELETE

def test_delete_character_success():
    # Agregar un personaje
    character_data = {
        "name": "Yoda",
        "height": 66,
        "mass": 17,
        "hair_color": "white",
        "skin_color": "green",
        "eye_color": "brown",
        "birth_year": 896
    }
    response = client.post("/character/add", json=character_data)
    character_id = response.json()["id"]
    
    response = client.delete(f"/character/delete/{character_id}")
    assert response.status_code == 200
    assert response.json() == {"detail": "Character deleted successfully"}

def test_delete_character_not_found():
    response = client.delete("/character/delete/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "Character not found"}
