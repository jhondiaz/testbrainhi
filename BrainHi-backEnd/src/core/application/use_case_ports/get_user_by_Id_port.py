from src.core.domain.entities.user import User
from src.core.domain.interfaces.repositorys.user_repository import IUserRepository
from src.core.application.use_cases.get_user_by_id import IGerUserById

class GetUserByIdPort(IGerUserById):
    def __init__(self, repository :IUserRepository):
        self.repository = repository

    async def execute(self, id:str)->User:
      return await self.repository.get(id)