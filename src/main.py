from fastapi import FastAPI
from flask_cors import CORS
from fastapi.middleware.cors import CORSMiddleware 
from routes import configure_routes
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todos los orígenes. Cambia esto a una lista específica para mayor seguridad.
    allow_credentials=True,  # Permitir el envío de cookies y credenciales
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

db = {}  # Simulación de base de datos
configure_routes(app, db)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)