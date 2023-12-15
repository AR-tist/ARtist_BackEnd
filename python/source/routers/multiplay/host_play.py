import time

from pymongo import MongoClient

async def hostPlay(event, connected_clients, rooms):
    room = rooms[event['room_id']]
    for guest in room.guests:
        await connected_clients[guest].send_text(
            str({'type': 'areYouReady', 'data': {}}).replace("'", '"')
        )
    client = MongoClient('mongodb://artist:1234@13.124.50.132:8484/')
    db = client['artist']
    collection = db['MidiFile']

    # increment 1 to play_count field
    collection.update_one({"filename": room.music_instance.filename}, {"$inc": {"views": 1}})

    print(f'{event["connectionID"]} - {event["nickname"]} command host Start in room {event["room_id"]}')
    
