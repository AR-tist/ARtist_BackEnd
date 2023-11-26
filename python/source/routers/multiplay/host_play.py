async def hostPlay(event, connected_clients, rooms):
    room = rooms[event['room_id']]
    for guest in room.guests:
        await connected_clients[guest].send_text(
            str({'type': 'host_play', 'data': {}}).replace("'", '"')
        )
    print(f'{event["connectionID"]} - {event["nickname"]} started playing')
    
    while True:
        all_loaded = True
        for guest in room.guests:
            if room.guests[guest].load_complete == 0:
                all_loaded = False
                continue
        
        if all_loaded:
            break
        
    for guest in room.guests:
        await connected_clients[guest].send_text(
            str({'type': 'start', 'data': {}}).replace("'", '"')
        )
        