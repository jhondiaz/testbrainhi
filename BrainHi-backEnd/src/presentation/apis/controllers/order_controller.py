from fastapi import APIRouter, status
from src.core.containers import container
from src.core.domain.interfaces.notifications.email_notification import IEmailNotification
from src.core.domain.interfaces.repositorys.user_repository import IUserRepository
from src.core.application.use_case_ports.create_user_port import CreateUserPort
from src.core.domain.entities.user import User
from src.core.domain.shemas.response_Model import ApiResponse
from src.core.application.use_case_ports.get_user_by_Id_port import GetUserByIdPort


orderApi = APIRouter(prefix="/api")
container = container.DependencyContainer()


@orderApi.post("/order/insert",response_model=ApiResponse,status_code=status.HTTP_200_OK)
async def logIn(user: User):
    repository = container.resolve(IUserRepository)
    email_service = container.resolve(IEmailNotification)
    result = await CreateUserPort(repository, email_service).execute(user)
    return ApiResponse(Value=result) 

 