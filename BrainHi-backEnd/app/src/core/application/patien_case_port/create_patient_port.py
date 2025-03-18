import hashlib
from src.core.domain.interfaces.repositorys.patient_repository import IPatientRepository
from src.core.domain.entities.patient import Patient
from src.core.application.patient_case.create_patient import ICreatePatient
from src.core.domain.shemas.response_repository import RepoResponse
from src.core.domain.interfaces.notifications.email_notification import IEmailNotification



class CreatePatientPort(ICreatePatient):
    def __init__(self, repository :IPatientRepository , emailNotification:IEmailNotification):
        self.repository = repository
        self.emailNotification=emailNotification

    async def execute(self, patient:Patient)->RepoResponse:
      try:
          
            result:RepoResponse=await self.repository.save(patient)

            if(result.IsSuccess):
              print(result)
              self.emailNotification.config("systemaf5@gmail.com")
              self.emailNotification.send(f"Paciente\n:{result.Value}",patient.email)
              return result  
            else:
             return result
            
      except Exception as e:
            return {"is_success": False, "message": f"Error: {str(e)}"}
