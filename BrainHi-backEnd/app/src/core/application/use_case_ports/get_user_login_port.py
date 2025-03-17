import hashlib
from src.core.application.use_cases.get_user_login import IGerUserLogIn
from src.core.domain.dtos.user_dto import UserDTO
from src.core.domain.interfaces.repositorys.user_repository import IUserRepository
from src.core.application.use_cases.get_user_by_email import IGerUserByEmail


class GetLogInPort(IGerUserLogIn):
    def __init__(self, repository: IUserRepository):
        self.repository = repository

    async def execute(self, email: str ,password:str) ->  UserDTO | None:
        user = await self.repository.getByEmail(email)
        print(user)
        if user.password== hashlib.sha256(password.encode('utf-8')).hexdigest():
            return UserDTO(
                id=user.id,
                email=user.email,
                firstName=user.firstName,
                lastName=user.lastName,
                phone=user.phone,
            )
        else : return None
