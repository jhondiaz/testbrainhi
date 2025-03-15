
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

try:
 
 client=MongoClient("mongodb+srv://systemaf5:KTyrK7Kfsb76NgcW@cluster0.ubtfw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

 client.admin.command('ping')
 print("🚀 Conexión exitosa a MongoDB")

 dataContext = client["brainhi"]

 userCollection = dataContext["users"]

except ConnectionFailure as e:
    print(f"❌ Error de conexión a MongoDB: {e}") 
