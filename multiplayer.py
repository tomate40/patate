import pymongo, os
import settings


client = pymongo.MongoClient(os.getenv('DATABASE'))

db = client['patate']
collection = db['patate']
    
def upload():
    collection.update_one({'_id': 'Player1'}, {'$set': {'x': settings.Xpos, 'y': settings.Ypos}})
    
def download():
    r = collection.find_one({'_id': 'Player2'})
    settings.Xpos2 = r['x']
    settings.Ypos2 = r['y']
    
def take_position():
    r = collection.find_one({'_id': 'Player1'})
    settings.Xpos = r['x']
    settings.Ypos = r['y']

    