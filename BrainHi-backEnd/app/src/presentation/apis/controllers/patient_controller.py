from datetime import datetime
import logging
from fastapi import APIRouter, Depends, HTTPException, status
from src.core.application.patien_case_port.get_by_id_patient_port import GetByIdPatientPort
from src.core.domain.auth.auth_bearer import JWTBearer
from src.core.application.patien_case_port.create_patient_port import CreatePatientPort
from src.core.domain.entities.patient import Patient
from src.core.domain.interfaces.repositorys.patient_repository import IPatientRepository
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


patientApi = APIRouter(prefix="/Api")
container = container.DependencyContainer()


@patientApi.get("/Patient/{id}",
                 response_model=ApiResponse,
                 status_code=status.HTTP_200_OK,
                 dependencies=[Depends(JWTBearer())],
                 tags=["posts"]
               )

async def getPatientById(id: str):
    try:
       
        repository = container.resolve(IPatientRepository)
        user = await GetByIdPatientPort(repository).execute(id)
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


@patientApi.post(
    "/Patient/Register", 
    response_model=ApiResponse, 
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(JWTBearer())],
    tags=["posts"]

)
async def createPatient(dato: Patient):
    try:
      
        repository = container.resolve(IPatientRepository)
        email_service = container.resolve(IEmailNotification)
        result = await CreatePatientPort(repository, email_service).execute(dato)
        if result:
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
