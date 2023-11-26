import logging


async def disconnect(event, connected_clients, rooms):
    if event['room_id'] not in rooms:
        return
    
    room = rooms[event['room_id']]
    
    del room.guests[event['connectionID']]

    for guest in room.guests:
        await connected_clients[guest].send_text(
            str({'type': 'disconnect', 'data': {'connectionID': event['connectionID']}}).replace("'", '"')
        )

    print(f'{event["connectionID"]} - {event["nickname"]} left room {event["room_id"]}')
    if len(room.guests) == 0:
        del rooms[event['room_id']]
        print(f'Room {event["room_id"]} deleted')

    if event['host']:
        tmp_guests = room.guests.copy()
        for guest in tmp_guests:
            await connected_clients[guest].close()

        
