from feature.user.domain.user import User  # Import User from the domain module
from feature.user.domain.user_repository_interface import UserRepositoryInterface

class UserService(UserRepositoryInterface):
    def __init__(self, user_repository):
        self.user_repository = user_repository

    async def create_user(self, id: str, name: str, email: str):
        # Crear una instancia de User
        user = User(id=id, name=name, email=email)
        # Guardar el usuario en el repositorio
        created_user = await self.user_repository.create_user(user)
        return created_user

    async def get_user_by_id(self, user_id: str):
        # Obtener un usuario por ID desde el repositorio
        user = await self.user_repository.get_user_by_id(user_id)
        return user

    async def get_users(self):
        # Obtener todos los usuarios desde el repositorio
        users = await self.user_repository.get_users()
        return users