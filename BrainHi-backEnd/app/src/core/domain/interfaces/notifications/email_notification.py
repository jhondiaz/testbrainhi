from abc import ABC, abstractmethod

# Definir la interfaz
class IEmailNotification(ABC):
    @abstractmethod
    def send(self, message: str, to: str):
        pass

    @abstractmethod
    def config(self, _from: str):
        pass