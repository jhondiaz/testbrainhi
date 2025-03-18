from typing import List, Optional
from uuid import UUID, uuid4
from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime

from src.core.domain.entities.human_name import HumanName



class Patient(BaseModel):
    id: Optional[str] = None
    name: List[HumanName]
    gender: Optional[str] = None
    birthDate: Optional[str] = None
    email: Optional[str] = None
   
class Config:
   json_encoders = {
            ObjectId: str
        }
   schema_extra={
      "ejemplo":{
         "firstName":"Jhon",
         "lastName":"Diaz",
         "phone":"+573103680445",
         "email":"systemaf5@gmail.com",
      }
   } 

