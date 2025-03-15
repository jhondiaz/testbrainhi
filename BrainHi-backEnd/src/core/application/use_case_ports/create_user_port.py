from src.core.domain.shemas.response_repository import RepoResponse
from src.core.domain.interfaces.notifications.email_notification import IEmailNotification
from src.core.domain.entities.user import User
from src.core.domain.interfaces.repositorys.user_repository  import IUserRepository
from src.core.application.use_cases.create_user import ICreateUser

from uuid import uuid4

class CreateUserPort(ICreateUser):
    def __init__(self, repository :IUserRepository , emailNotification:IEmailNotification):
        self.repository = repository
        self.emailNotification=emailNotification

    async def execute(self, user:User)->RepoResponse:
      try:
            result:RepoResponse=await self.repository.save(user)

            if(result.IsSuccess):
              print(result)
              self.emailNotification.config("systemaf5@gmail.com")
              self.emailNotification.send(f"Usuario registrado exitosamente:{user.firstName} {user.lastName}",user.email)
              return result  
            else:
             return result
            
      except Exception as e:
            return {"is_success": False, "message": f"Error: {str(e)}"}
