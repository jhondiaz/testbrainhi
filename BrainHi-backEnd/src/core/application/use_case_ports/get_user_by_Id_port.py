from src.core.domain.dtos.user_dto import UserDTO
from src.core.domain.entities.user import User
from src.core.domain.interfaces.repositorys.user_repository import IUserRepository
from src.core.application.use_cases.get_user_by_id import IGerUserById


class GetUserByIdPort(IGerUserById):
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    async def execute(self, id: str) -> UserDTO | None:
        user = await self.repository.getById(id)
        return UserDTO(
            id=user.id,
            email=user.email,
            firstName=user.firstName,
            lastName=user.lastName,
            phone=user.phone,
        )
