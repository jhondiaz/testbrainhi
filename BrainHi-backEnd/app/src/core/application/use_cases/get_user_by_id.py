
from abc import ABC,abstractmethod

from src.core.domain.dtos.user_dto import UserDTO



class IGerUserById(ABC):
   @abstractmethod
   async def execute(self, id: str) ->UserDTO| None:
      pass 