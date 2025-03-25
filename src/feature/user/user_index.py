from fastapi import APIRouter, Body, Path
from feature.user.infrastructure.api.user_controller import UserController
from feature.user.application.user_uses_cases import UserUseCases
from feature.user.infrastructure.api.user_service import UserService
from feature.user.infrastructure.persistence.user_repository import UserRepository
from feature.user.application.user_dtos import UserCreateRequest


def get_user_router(db):
    router = APIRouter(tags=["Users"])

    # Configuración de dependencias
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    user_use_cases = UserUseCases(user_service)
    user_controller = UserController(user_use_cases)

    @router.post(
        "/createuser",
        summary="Create a new user",
        description="Creates a new user with the provided name and email"
    )
    async def create_user(user: UserCreateRequest = Body(...)):
        return await user_controller.create_user(user)

    @router.get(
        "/getuser/{user_id}",
        summary="Get user by ID",
        description="Retrieves a user by their unique identifier"
    )
    async def get_user_by_id(
        user_id: str = Path(..., title="User ID", description="The unique identifier of the user")
    ):
        return await user_controller.get_user_by_id(user_id)

    @router.get(
        "/getusers",
        summary="Get all users",
        description="Retrieves all users in the system"
    )
    async def get_users():
        return await user_controller.get_users()

    return router