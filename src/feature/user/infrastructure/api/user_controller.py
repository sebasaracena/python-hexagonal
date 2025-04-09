from fastapi import  HTTPException
from uuid import uuid4
from feature.user.application.user_dtos import UserCreateRequest,UserResponse

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
        user_response = UserResponse.from_domain(created_user)   
        return {"status": 200, "user": user_response.dict()}

    async def get_user_by_id(self, user_id):
        # Extraer el ID de usuario de los parámetros de consulta
        user_id = user_id
       # Obtener el usuario por ID
        user = await self.user_use_cases.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"status": 200, "user": UserResponse.from_domain(user).dict()}

    async def get_users(self):
        # Obtener todos los usuarios
        users = await self.user_use_cases.get_users()
        return {"status": 200, "users": [UserResponse.from_domain(user).dict() for user in users]}
    
    async def update_user(self, user_data:UserResponse):
        # Extraer datos del cuerpo de la solicitud
        user_id = user_data.id
        name = user_data.name
        email = user_data.email

        if not user_id or not name or not email:
            raise HTTPException(status_code=400, detail="Faltan campos obligatorios: id, name o email")

        # Actualizar el usuario
        updated_user = await self.user_use_cases.update_user(user_id, name, email)
        if not updated_user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"status": 200, "user": UserResponse.from_domain(updated_user).dict()}
    
    async def delete_user(self, user_id):
        # Extraer el ID de usuario de los parámetros de consulta
        user_id = user_id
        # Eliminar el usuario por ID
        deleted_user = await self.user_use_cases.delete_user(user_id)
        if not deleted_user:
            raise HTTPException(status_code=404, detail="Usuario no encontrado")
        return {"status": 200, "message": "Usuario eliminado correctamente"}