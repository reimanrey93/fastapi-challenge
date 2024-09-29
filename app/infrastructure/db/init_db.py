from .database import engine
from app.domain.models import Character, Base

def init_db():
    Base.metadata.create_all(bind=engine)
