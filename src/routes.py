from fastapi import FastAPI
from feature.user.infrastructure.api.user_routes import get_user_router

def configure_routes(app: FastAPI, db: dict):
    """Configure all application routes"""
    app.include_router(
        get_user_router(db), 
        prefix="/api/user"
    )