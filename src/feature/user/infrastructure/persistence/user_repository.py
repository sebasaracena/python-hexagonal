class UserRepository:
    def __init__(self, db):
        self.db = db
        self.users = []

    async def create_user(self, user):
        # Agregar el usuario a la lista
        self.users.append(user)
        return user

    async def get_user_by_id(self, user_id):
        # Buscar un usuario por su ID
        for user in self.users:
            if user.id == user_id:
                return user
        return None

    async def get_users(self):
        # Retornar todos los usuarios
        return self.users