from fastapi import FastAPI
from feature.user.user_index import get_user_router
from routes import configure_routes
app = FastAPI()
db = {}  # Simulación de base de datos
configure_routes(app, db)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)