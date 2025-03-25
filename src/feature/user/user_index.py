from fastapi import APIRouter, Request
from feature.user.infrastructure.api.user_controller import UserController
from feature.user.application.user_uses_cases import UserUseCases
from feature.user.infrastructure.api.user_service import UserService
from feature.user.infrastructure.persistence.user_repository import UserRepository

def get_user_router(db):
    router = APIRouter()

    # Configuración de dependencias
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    user_use_cases = UserUseCases(user_service)
    user_controller = UserController(user_use_cases)

    # Rutas
    @router.post("/createuser")
    async def create_user(request: Request):
        return await user_controller.create_user(request)

    @router.get("/getuser")
    async def get_user_by_id(request: Request):
        return await user_controller.get_user_by_id(request)

    @router.get("/getusers")
    async def get_users():
        return await user_controller.get_users()

    return router