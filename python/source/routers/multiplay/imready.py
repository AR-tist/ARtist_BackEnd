import time
from datetime import datetime

async def imready(event, connected_clients, rooms):
    room = rooms[event['room_id']]
    
    room.guests[event['connectionID']].load_complete = 1
    
    print(f'{event["connectionID"]} - {event["nickname"]} is ready in room {event["room_id"]}')
    
    all_loaded = True
    
    for guest in room.guests:
        if room.guests[guest].load_complete == 0:
            all_loaded = False
            continue
    
    if all_loaded:
        now = int(datetime.now().timestamp() * 1000) # milliseconds since epoch
        for guest in room.guests:
            await connected_clients[guest].send_text(
                str({'type': 'start', 'data': {now}}).replace("'", '"')
            )
        print(f'{event["connectionID"]} - {event["room_id"]} loading Complition and Start')