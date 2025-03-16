from src.core.domain.shemas.response_repository import RepoResponse
from src.core.domain.entities.user import User
from src.core.domain.interfaces.repositorys.user_repository import IUserRepository
from src.insfrastructure.datacontext.mongo_data_context import userCollection 
from bson import ObjectId,errors
from pymongo.errors import ConnectionFailure

class UserRepository(IUserRepository):
   
    async def save(self, user: User)->RepoResponse:
     try:  
       user_dict = user.model_dump() 
       del user_dict["id"]
       userCollection.insert_one(user_dict)
       return RepoResponse(IsSuccess=True, Value="Ok")
     except ConnectionFailure as e:
       return RepoResponse(IsSuccess=False, Value="Error : {e}")

    

    async def getById(self, id: str)->User| None:
         try:
          object_id = ObjectId(id)  # Convertir el ID
          user = userCollection.find_one({"_id": object_id})
          if user:
              user["password"]=str("-") 
              user["id"] = str(user["_id"]) 
              return User(**user)
         except errors.InvalidId:
          return None           
         
   
    async def getByEmail(self, email: str)->User| None:
         try:
          user = userCollection.find_one({"email": email})
          if user:
              user["id"] = str(user["_id"]) 
              return User(**user)             
         except errors:
          return None           

  