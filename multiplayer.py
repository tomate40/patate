import pymongo
import os
import settings
    
def upload():
    collection.update_one({'_id': 'Player1'}, {'$set': {'x': settings.Xpos, 'y': settings.Ypos}})
    
def download():
    u = collection.find_one({'_id': 'Player2'})
    settings.Xpos2 = u['x']
    settings.Ypos2 = u['y']
    
def take_position():
	o = collection.find_one({'_id': 'Player1'})
	settings.Xpos = o['x']
	settings.Ypos = o['y']

def positioningP2():
    f = collection.find_one({'_id': 'Player2'})
    settings.Xpos2 = f['x']
    settings.Ypos2 = f['y']

def Attaque(X, Y):
	collection.update_one({"_id": "Player1"}, {"$set": {"attaqueX": X, "attqueY": Y}})


def initMultiplayer():
    global collection
    print("ge")
    client = pymongo.MongoClient(os.getenv('DATABASE'))

    db = client['patate']
    collection = db['patate']