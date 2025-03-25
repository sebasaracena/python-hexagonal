# Arquitectura Hexagonal en Python - Implementación

## Estructura del Proyecto

Este proyecto implementa la Arquitectura Hexagonal usando FastAPI, demostrando una clara separación de responsabilidades en la gestión de usuarios.

### Capas de la Arquitectura

#### 1. Dominio
- `user.py`: Define la entidad User usando Pydantic
- `user_repository_interface.py`: Define el puerto principal para operaciones de usuario

#### 2. Aplicación
- `user_uses_cases.py`: Implementa la lógica de negocio para operaciones de usuario
- `user_service.py`: Conecta casos de uso con el repositorio

#### 3. Infraestructura
- `user_controller.py`: Maneja las peticiones HTTP
- `user_repository.py`: Implementa la persistencia de usuarios
- `user_index.py`: Configura las rutas y dependencias

## Estructura de Carpetas

```
src/
├── feature/user/
│   ├── domain/
│   │   ├── user.py
│   │   └── user_repository_interface.py
│   ├── application/
│   │   └── user_dtos.py
│   │   └── user_uses_cases.py
│   └── infrastructure/
│       ├── api/
│       │   ├── user_controller.py
│       │   └── user_service.py
│       └── persistence/
│           └── user_repository.py
└── main.py
```

## Endpoints API

- POST `/api/user/createuser`: Crear nuevo usuario
- GET `/api/user/getuser`: Obtener usuario por ID
- GET `/api/user/getusers`: Listar todos los usuarios

## Tecnologías Utilizadas

- FastAPI para la API REST
- Pydantic para validación de datos
- Uvicorn como servidor ASGI



