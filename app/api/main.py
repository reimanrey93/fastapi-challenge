from fastapi import FastAPI
from app.api.v1.endpoints import characters  # Importa tus rutas
from app.infrastructure.db.init_db import init_db  # Importa la inicialización de la BD

app = FastAPI()

# Inicializa la base de datos creando las tablas
init_db()

# Incluir las rutas de la API
app.include_router(characters.router, prefix="/api/v1")

