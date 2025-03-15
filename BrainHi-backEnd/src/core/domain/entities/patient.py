from typing import Optional
from uuid import UUID, uuid4
from bson import ObjectId
from pydantic import BaseModel
from datetime import datetime

class Patient(BaseModel):
   id: Optional[str]
   firstName: str
   lastName: str
   gender: str
   birthDate:Optional[datetime]=datetime.now()
   phone: str
   email: str
   createDate:Optional[datetime]=datetime.now()
   
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

