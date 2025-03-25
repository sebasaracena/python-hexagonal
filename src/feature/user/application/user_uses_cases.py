class UserUseCases:
    def __init__(self, user_service):
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