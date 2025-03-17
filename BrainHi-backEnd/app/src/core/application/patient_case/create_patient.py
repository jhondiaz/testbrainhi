
from abc import ABC,abstractmethod

from src.core.domain.entities.patient import Patient
from src.core.domain.entities.user import User


class ICreatePatient(ABC):
 
 @abstractmethod
 async def execute(self, patient: Patient)->int:
      pass 