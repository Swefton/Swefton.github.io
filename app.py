from flask import Flask, render_template, request,jsonify 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import random
import json

uri = ""
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/events')
def index():
    db = client['events']
    coll = db["deets"]
    data = coll.find()
    sol = []
    for document in coll.find():
        sol.append([document['location'], document['attending'], document['space'], document['lat'], document['lon'], document['sec']])
    return render_template('events.html', data=sol)

@app.route('/login', methods=['POST'])
def process_input():
    # Retrieve the user's input from the form data
    secret_key = request.form['secretkey']
    db = client['events']
    coll = db["deets"]
    event_keys = [str(x) for x in coll.distinct('sec')]
    if secret_key in event_keys:
        event_details = coll.find_one({'sec': int(secret_key)})
        print(event_details)
        return render_template('organizer-event.html', data=event_details)
    else:
        return render_template('not-found.html')

@app.route('/create-event')
def create_event():
    return render_template('create-event.html')

@app.route('/create-event-submit', methods=['POST'])
def submit_event():
    event_name = request.form['eventname']
    hashK = hash(event_name)
    lat = request.form['lat']
    long = request.form['long']

    item = {
    "_id": random.randint(2, 1000000),
    "sec": hashK,
    "location": event_name,
    "lat": float(lat),
    "lon": float(long),
    "announcements": [],
    "attending": 0,
    "space": 999,
    "waitlist": 0,
    }
    db = client['events']
    coll = db["deets"]
    coll.insert_many([item])
    return render_template('create-event-ann.html',announcement=item['sec'])

@app.route('/organizer-login.html')
def organizer_login():
    return render_template('organizer-login.html')

@app.route('/update-db')
def update_db():
    db = client['events']
    coll = db["deets"]
    return render_template('organizer-login.html')

@app.route('/map')
def map():
    db = client['events']
    coll = db["deets"]
    data = coll.find()
    sol = []
    for document in coll.find():
        sol.append([document['location'], document['attending'], document['space'], document['lat'], document['lon'], document['sec']])
    return render_template('map.html', data=sol)

if __name__ == '__main__':
    app.run(debug=True)
