from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "" # uri here

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    
    db = client['people']
    coll = db["users"]
    
    item = {
        "_id": 1,
        "user": "sheep",
        "loca": "314"
    }
    
    coll.insert_many([item])
    
    print("cowoc")
    
except Exception as e:
    print(e)
