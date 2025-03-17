
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class UserDTO(BaseModel):
   id: Optional[str]
   firstName: str
   lastName: str
   phone: str
   email: str
   createDate:Optional[datetime]=datetime.now()