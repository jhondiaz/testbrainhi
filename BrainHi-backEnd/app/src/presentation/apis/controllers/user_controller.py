from datetime import datetime
import logging
from fastapi import APIRouter, HTTPException, status
from src.core.domain.dtos.register_user_dto import RegisterUserDTO
from src.core.containers import container
from src.core.domain.interfaces.notifications.email_notification import (
    IEmailNotification,
)
from src.core.domain.interfaces.repositorys.user_repository import IUserRepository
from src.core.application.use_case_ports.create_user_port import CreateUserPort
from src.core.domain.entities.user import User
from src.core.domain.shemas.response_Model import ApiResponse
from src.core.application.use_case_ports.get_user_by_Id_port import GetUserByIdPort


userApi = APIRouter(prefix="/Api")
container = container.DependencyContainer()


@userApi.get("/User/{id}", response_model=ApiResponse, status_code=status.HTTP_200_OK)
async def getUserById(id: str):
    try:
       
        repository = container.resolve(IUserRepository)
        user = await GetUserByIdPort(repository).execute(id)
        return ApiResponse(Value=user)

    except ValueError as ve:
        logging.error(f"Error de validación: {ve}")
        return ApiResponse(Value=None, Codigo=1, Message="Error de validación")

    except ConnectionError as ce:
        logging.error(f"Error de conexión: {ce}")
        return ApiResponse(Value=None, Codigo=2, Message="Error de conexión con el servidor")

    except Exception as e:
        logging.error(f"Error inesperado: {e}", exc_info=True)  # Registra el stack trace completo
        return ApiResponse(Value=None, Codigo=3, Message="Error inesperado, intente nuevamente")


@userApi.post(
    "/User/Register", response_model=ApiResponse, status_code=status.HTTP_200_OK
)
async def createUser(dato: RegisterUserDTO):
    try:

        user: User = User(
            id="",
            firstName=dato.firstName,
            lastName=dato.lastName, 
            email=dato.email,
            phone=dato.phone,
            createDate=datetime.now(),
            password=dato.password
        )

        repository = container.resolve(IUserRepository)
        email_service = container.resolve(IEmailNotification)
        result = await CreateUserPort(repository, email_service).execute(user)
        return ApiResponse(
            Value=result.Value, IsSuccess=result.IsSuccess, Message=result.Message
        )
    
    except ValueError as ve:
        logging.error(f"Error de validación: {ve}")
        return ApiResponse(Value=None, Codigo=1, Message="Error de validación")

    except ConnectionError as ce:
        logging.error(f"Error de conexión: {ce}")
        return ApiResponse(Value=None, Codigo=2, Message="Error de conexión con el servidor")

    except Exception as e:
        logging.error(f"Error inesperado: {e}", exc_info=True) 
        return ApiResponse(Value=None, Codigo=3, Message="Error inesperado, intente nuevamente")
