from pymongo import MongoClient
from pymongo.database import Database


# mongo_uri: str = "mongodb://localhost:27017"
mongo_uri: str = "mongodb+srv://info802:usMbf0€ver@cluster0.mmmmu.mongodb.net/Cars?retryWrites=true&w=majority"
client: MongoClient = MongoClient(mongo_uri)
db: Database = client["Cars"]
