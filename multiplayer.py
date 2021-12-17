import pymongo, os
import settings
import player2


client = pymongo.MongoClient(os.getenv('DATABASE'))

db = client['patate']
collection = db['patate']
    
def upload():
    collection.update_one({'_id': 'Player1'}, {'$set': {'x': settings.Xpos, 'y': settings.Ypos}})
    
def download():
    r = collection.find_one({'_id': 'Player2'})
    settings.Xpos2 = r['x']
    settings.Ypos2 = r['y']
    player2.p2.rectangle_player2.x = r['x']
    player2.p2.rectangle_player2.y = r['y']
    
