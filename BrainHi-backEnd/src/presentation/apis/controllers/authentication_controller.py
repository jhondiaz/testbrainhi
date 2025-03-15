from datetime import datetime, timedelta
from fastapi import APIRouter, HTTPException, status
from src.core.domain.dtos.login_dto import LoginDTO
from src.core.containers import container
from src.core.domain.interfaces.notifications.email_notification import IEmailNotification
from src.core.domain.interfaces.repositorys.user_repository import IUserRepository
from src.core.application.use_case_ports.create_user_port import CreateUserPort
from src.core.domain.entities.user import User
from src.core.domain.shemas.response_Model import ApiResponse
from src.core.application.use_case_ports.get_user_by_Id_port import GetUserByIdPort
from jose import jwt

authenticationApi = APIRouter(prefix="/api")
container = container.DependencyContainer()

SECRET_KEY = "tu_clave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def _create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


@authenticationApi.post("/authentication/login",response_model=ApiResponse,status_code=status.HTTP_200_OK)
async def login(user: LoginDTO):
    try:
        repository = container.resolve(IUserRepository)
        email_service = container.resolve(IEmailNotification)
        result = await CreateUserPort(repository, email_service).execute(user)
        return ApiResponse(Value=result) 
    except:
      raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Passsword incorecto")
       

 