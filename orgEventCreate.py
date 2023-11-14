from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import random

uri = ""
client = MongoClient(uri, server_api=ServerApi('1'))

def create():
    locName = input()
    hashK = hash(locName)
    lat = float(input())
    lon = float(input())
    

    db = client['events']
    coll = db["deets"]
        
    item = {
        "_id": random.randint(2, 1000000),
        "sec": hashK,
        "location": locName,
        "lat": lat,
        "lon": lon,
        "announcements": [],
        "attending": 0,
        "space": 999,
        "waitlist": 0,
    }
    
    coll.insert_many([item])
    

def search():
    db = client['events']
    coll = db["deets"]
    document = coll.find_one({'sec': 1817557989549621983})
    events = coll.distinct('sec')
    
    db = client['events']
    coll = db["deets"]

    for document in coll.find():
        print(document)
    
    # {'_id': 729068, 'sec': 4994436083811529148, 'location': 'MadHacks', 'lat': 47.0, 'lon': 43.2, 'announcements': [], 'attending': 0, 'space': 999, 'waitlist': 0}
    


search()
