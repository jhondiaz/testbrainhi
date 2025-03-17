
from abc import ABC,abstractmethod

from src.core.domain.dtos.user_dto import UserDTO



class IGerUserLogIn(ABC):
   @abstractmethod
   async def execute(self, email: str, password: str) ->UserDTO| None:
      pass 