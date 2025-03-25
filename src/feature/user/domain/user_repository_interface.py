from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    async def create_user(self, user):
        """Create a new user"""
        raise NotImplementedError("Method create_user not implemented")

    @abstractmethod
    async def get_user_by_id(self, id):
        """Get user by id"""
        raise NotImplementedError("Method get_by_id not implemented")

    @abstractmethod
    async def get_users(self):
        """Get all users"""
        raise NotImplementedError("Method get_users not implemented")