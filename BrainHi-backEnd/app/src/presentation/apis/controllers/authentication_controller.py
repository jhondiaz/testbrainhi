from datetime import datetime, timedelta
import hashlib
import logging
import time
from fastapi import APIRouter, HTTPException, status
from src.core.domain.auth.auth_handler import decodeJWT, signJWT
from src.core.application.use_case_ports.get_user_login_port import GetLogInPort
from src.core.domain.dtos.login_dto import LoginDTO
from src.core.containers import container
from src.core.domain.interfaces.repositorys.user_repository import IUserRepository
from src.core.domain.shemas.response_Model import ApiResponse
from jose import ExpiredSignatureError, JWTError, jwt

authenticationApi = APIRouter(prefix="/Api")
container = container.DependencyContainer()

@authenticationApi.post(
    "/Authentication/LogIn", response_model=ApiResponse, status_code=status.HTTP_200_OK
)
async def login(user: LoginDTO):
    repository = container.resolve(IUserRepository)
    userResult = await GetLogInPort(repository).execute(user.email, user.password)
 
    if userResult:
        token = signJWT(userResult)

        return ApiResponse(Value={"token": token, "user": userResult.model_dump()})
    else:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Passsword incorecto"
        )



@authenticationApi.get(
    "/Authentication/SignInUsingToken", response_model=ApiResponse, status_code=status.HTTP_200_OK
)
def  SignInUsingToken(token: str) -> bool :
        try:
            payload = decodeJWT(token)
            if not payload:
                return ApiResponse(Value=False)
            
            return ApiResponse(Value=True)

        except ExpiredSignatureError as ex:
             logging.error(f"Error: {ex}")
             return ApiResponse(Value=False)
        except JWTError as ex:
             logging.error(f"Error: {ex}")
             return ApiResponse(Value=False)
        
  