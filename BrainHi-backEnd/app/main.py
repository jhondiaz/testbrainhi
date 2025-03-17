from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from src.core.domain.interfaces.repositorys.patient_repository import IPatientRepository
from src.insfrastructure.repositories.patient.patient_repository import PatientRepository
from src.core.containers.container import DependencyContainer
from src.core.domain.interfaces.notifications.email_notification import (
    IEmailNotification,
)
from src.core.domain.interfaces.repositorys.user_repository import IUserRepository
from src.insfrastructure.notifications.email_notification import EmailNotification
from src.insfrastructure.repositories.users.user_repository import UserRepository
from src.presentation.apis.controllers.user_controller import userApi
from src.presentation.apis.controllers.patient_controller import patientApi
from src.presentation.apis.controllers.authentication_controller import (
    authenticationApi,
)
from jose import jwt, JWTError

app = FastAPI(
    title="Api testBranhi",
    version="0.0.2",
    
)
app.state.data = {}

container = DependencyContainer()
container.register(IUserRepository, UserRepository)
container.register(IPatientRepository, PatientRepository)
container.register(IEmailNotification, EmailNotification)

origins = [
   "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def read_root():
    app.state.data.clear()
    return {"Hello": "BRAINHI", "vs": "04"}


# UI de usuarios
app.include_router(authenticationApi)
app.include_router(userApi)
app.include_router(patientApi)

