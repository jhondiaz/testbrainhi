from abc import ABC, abstractmethod

from src.core.domain.entities.patient import Patient
from src.core.domain.shemas.response_repository import RepoResponse


class IPatientRepository(ABC):
    @abstractmethod
    def save(self, patient :Patient) ->RepoResponse:
      pass

    @abstractmethod
    def getById(self, id:str) ->Patient:
      pass

