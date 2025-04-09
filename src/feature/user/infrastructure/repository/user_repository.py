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
    
    async def update_user(self, get_user):
        # Buscar el usuario por su ID y actualizarlo
        for user in self.users:
            if user.id == get_user.id:
                user.name = get_user.name
                user.email = get_user.email
                # Guardar los cambios en la base de datos (simulado aquí)
                return user
        return 
    
    async def delete_user(self, user_id):
        # Buscar el usuario por su ID y eliminarlo
        for user in self.users:
            if user.id == user_id:
                self.users.remove(user)
                return user
        return None