
from pydantic import BaseModel


class RegisterUserDTO(BaseModel):
   firstName: str
   lastName: str
   phone: str
   email: str
   password: str
