async def disconnect(event, connected_clients, rooms):
    room = rooms[event['room_id']]
    del room.guests[event['connectionID']]

    if len(room.guests) == 0:
        del rooms[event['room_id']]

    if event['host']:
        tmp_guests = room.guests.copy()
        for guest in tmp_guests:
            await connected_clients[guest].close()

        
