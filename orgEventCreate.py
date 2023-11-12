from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import random

locName = input()
lat = float(input())
lon = float(input())
hashK = hash(locName)


uri = ""

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

    
db = client['events']
coll = db["deets"]
    
item = {
    "_id": random.randint(2, 1000000),
    "location": locName,
    "lat": lat,
    "lon": lon,
    "sec": hashK
}
    
coll.insert_many([item])
    
    
