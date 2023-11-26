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
        for guest in room.guests:
            await connected_clients[guest].send_text(
                str({'type': 'start', 'data': {}}).replace("'", '"')
            )
        print(f'{event["connectionID"]} - {event["room_id"]} loading Complition')