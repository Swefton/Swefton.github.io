from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = ""
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['people']


# Create a new client and connect to the server
#client = MongoClient(uri, server_api=ServerApi('1'))

try:
    #client.admin.command('ping')
    #print("Pinged your deployment. You successfully connected to MongoDB!")
    
    db = get_database()
    coll = db["users"]
    
    ideets = coll.find()
    
    print(ideets)
    
    for i in ideets:
        print(i)
    
    print("cowoc")
    
except Exception as e:
    print(e)
