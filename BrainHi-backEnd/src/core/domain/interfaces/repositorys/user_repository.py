from abc import ABC, abstractmethod

from src.core.domain.shemas.response_repository import RepoResponse
from src.core.domain.entities.user import User

class IUserRepository(ABC):
    @abstractmethod
    def save(self, user :User) ->RepoResponse:
      pass

    @abstractmethod
    def get(self, id:str) ->User:
      pass