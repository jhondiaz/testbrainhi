
from abc import ABC,abstractmethod

from src.core.domain.entities.patient import Patient
from src.core.domain.entities.user import User


class IGetByIdPatient(ABC):
 
 @abstractmethod
 async def execute(self, id: str)->int:
      pass 