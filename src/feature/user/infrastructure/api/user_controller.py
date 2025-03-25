from fastapi import  HTTPException, Request
from uuid import uuid4
from feature.user.application.user_dtos import UserCreateRequest

class UserController:
    def __init__(self, user_use_cases):
        self.user_use_cases = user_use_cases

    async def create_user(self, user_data: UserCreateRequest):
        # Extraer datos del cuerpo de la solicitud
        
        name = user_data.name
        email = user_data.email
      
        if not name or not email:
            raise HTTPException(status_code=400, detail="Faltan campos obligatorios: name o email")

        # Generar un ID único
        user_id = str(uuid4())

        # Crear el usuario
        created_user = await self.user_use_cases.create_user(user_id, name, email)
        return {"status": 201, "user": created_user}

    async def get_user_by_id(self, user_id):
        # Extraer el ID de usuario de los parámetros de consulta
        user_id = user_id
       # Obtener el usuario por ID
        user = await self.user_use_cases.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"status": 200, "user": user}

    async def get_users(self):
        # Obtener todos los usuarios
        users = await self.user_use_cases.get_users()
        return {"status": 200, "users": users}