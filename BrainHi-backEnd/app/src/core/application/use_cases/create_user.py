
from abc import ABC,abstractmethod

from src.core.domain.entities.user import User


class ICreateUser(ABC):
 
 @abstractmethod
 async def execute(self, user: User)->int:
      pass 