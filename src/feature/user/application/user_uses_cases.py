from feature.user.domain.user_repository_interface import UserRepositoryInterface

class UserUseCases:
    def __init__(self, user_service: UserRepositoryInterface):
        self.user_service = user_service

    async def create_user(self, id: str, name: str, email: str):
        # Llama al servicio para crear un usuario
        created_user = await self.user_service.create_user(id, name, email)
        return created_user

    async def get_user_by_id(self, user_id: str):
        # Llama al servicio para obtener un usuario por ID
        user = await self.user_service.get_user_by_id(user_id)
        return user

    async def get_users(self):
        # Llama al servicio para obtener todos los usuarios
        users = await self.user_service.get_users()
        return users
    
    async def update_user(self, user_id: str, name: str, email: str):
        # Llama al servicio para actualizar un usuario existente
        updated_user = await self.user_service.update_user(user_id, name, email)
        return updated_user
    
    async def delete_user(self, user_id: str):
        # Llama al servicio para eliminar un usuario por ID
        deleted_user = await self.user_service.delete_user(user_id)
        return deleted_user