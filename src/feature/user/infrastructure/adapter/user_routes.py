from fastapi import APIRouter, Body, Path
from feature.user.infrastructure.api.user_controller import UserController
from feature.user.application.user_uses_cases import UserUseCases
from feature.user.infrastructure.adapter.user_repository_impl import UserRepositoryImpl
from feature.user.infrastructure.repository.user_repository import UserRepository
from feature.user.application.user_dtos import UserCreateRequest,UserResponse


def get_user_router(db):
    router = APIRouter(tags=["Users"])

    # Configuración de dependencias
    user_repository = UserRepository(db)
    user_service =  UserRepositoryImpl(user_repository)
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

    @router.put(
        "/updateuser",
        summary="Update user",
        description="Updates an existing user with the provided name and email"
    )
    async def update_user(
        user: UserResponse = Body(...)
    ):
        return await user_controller.update_user(user)
    
    @router.delete(
        "/deleteuser/{user_id}",
        summary="Delete user",
        description="Deletes a user by their unique identifier"
    )
    async def delete_user(
        user_id: str = Path(..., title="User ID", description="The unique identifier of the user")
    ):
        return await user_controller.delete_user(user_id)

    return router