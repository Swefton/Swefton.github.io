from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import random

locName = input()
lat = float(input())
lon = float(input())
hashK = hash(locName)


uri = "mongodb+srv://backupofamrittoo:5aoCkc2tOsvpgkfx@amtesting.imkz74p.mongodb.net/?retryWrites=true&w=majority"
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
    
document = coll.find_one({'sec': 1817557989549621983})

events = coll.distinct('sec')
if 1817557989549621983 in events:
    print(coll.find_one({'sec': 1817557989549621983}))
else:
    print('not found')