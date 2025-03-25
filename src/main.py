from fastapi import FastAPI
from feature.user.user_index import get_user_router

app = FastAPI()
db = {}  # Simulación de base de datos
app.include_router(get_user_router(db), prefix="/api/user")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=3000)