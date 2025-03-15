
from abc import ABC,abstractmethod

from  src.core.domain.entities.user import User


class IGerUserById(ABC):
   @abstractmethod
   async def execute(self, id: str) ->User:
      pass 