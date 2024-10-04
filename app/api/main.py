from fastapi import FastAPI
from app.api.v1.endpoints import characters  
from app.infrastructure.db.init_db import init_db  
from fastapi.staticfiles import StaticFiles
from fastapi.openapi.docs import get_swagger_ui_html

app = FastAPI(
    title="Star Wars API",
    description="May the force be with you",
    version="1.0.0"
)

# Inicializa BD
init_db()

# Importa rutas de API
app.include_router(characters.router, prefix="/api/v1")

app.mount("/static", StaticFiles(directory="app/utils/media"), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        swagger_favicon_url="/static/scienceandfiction-roll_99278.png", 
        swagger_ui_parameters={"docExpansion": "none"} 
    )