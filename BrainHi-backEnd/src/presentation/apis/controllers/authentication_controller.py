from datetime import datetime, timedelta
import hashlib
import logging
import time
from fastapi import APIRouter, HTTPException, status
from src.core.application.use_case_ports.get_user_login_port import GetLogInPort
from src.core.domain.dtos.login_dto import LoginDTO
from src.core.containers import container
from src.core.domain.interfaces.repositorys.user_repository import IUserRepository
from src.core.domain.shemas.response_Model import ApiResponse
from jose import ExpiredSignatureError, JWTError, jwt

authenticationApi = APIRouter(prefix="/Api")
container = container.DependencyContainer()

SECRET_KEY = "tu_clave_secreta"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


@authenticationApi.post(
    "/Authentication/LogIn", response_model=ApiResponse, status_code=status.HTTP_200_OK
)
async def login(user: LoginDTO):
    ## try:
    print(user)
    repository = container.resolve(IUserRepository)
    userResult = await GetLogInPort(repository).execute(user.email, user.password)
  
    if userResult:
        expire = time.time() + ACCESS_TOKEN_EXPIRE_MINUTES
        token = jwt.encode(
            {
                "id": userResult.id,
                "name": f"{userResult.firstName} {userResult.lastName}",
                "iat": time.time(),
                "exp": expire,
            },
            SECRET_KEY,
            algorithm=ALGORITHM,
        )
        return ApiResponse(Value={"token": token, "user": userResult.model_dump()})
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Passsword incorecto"
        )


## except:
##   return HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Passsword incorecto")


@authenticationApi.get(
    "/Authentication/SignInUsingToken", response_model=ApiResponse, status_code=status.HTTP_200_OK
)
def  SignInUsingToken(token: str) -> bool :
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            if "exp" in payload and datetime.utcfromtimestamp(payload["exp"]) < datetime.utcnow():
                return ApiResponse(Value=False)
            
            return ApiResponse(Value=True)

        except ExpiredSignatureError as ex:
             logging.error(f"Error: {ex}")
             return ApiResponse(Value=False)
        except JWTError as ex:
             logging.error(f"Error: {ex}")
             return ApiResponse(Value=False)
        
  