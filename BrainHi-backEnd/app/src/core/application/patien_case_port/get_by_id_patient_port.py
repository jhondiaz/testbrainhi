import hashlib
from src.core.application.patient_case.get_by_id_patient import IGetByIdPatient
from src.core.domain.interfaces.repositorys.patient_repository import IPatientRepository
from src.core.domain.entities.patient import Patient
from src.core.domain.shemas.response_repository import RepoResponse
from src.core.domain.interfaces.notifications.email_notification import IEmailNotification



class GetByIdPatientPort(IGetByIdPatient):
    def __init__(self, repository :IPatientRepository ):
        self.repository = repository
    

    async def execute(self, id:str)->RepoResponse:
      try:
          
            result:RepoResponse=await self.repository.getById(id)
            return result
            
      except Exception as e:
            return {"is_success": False, "message": f"Error: {str(e)}"}
