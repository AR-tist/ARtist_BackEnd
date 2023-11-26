import time

async def hostPlay(event, connected_clients, rooms):
    room = rooms[event['room_id']]
    for guest in room.guests:
        await connected_clients[guest].send_text(
            str({'type': 'areYouReady', 'data': {}}).replace("'", '"')
        )
    print(f'{event["connectionID"]} - {event["nickname"]} command host Start in room {event["room_id"]}')
    
