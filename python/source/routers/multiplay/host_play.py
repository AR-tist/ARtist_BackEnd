import time

async def hostPlay(event, connected_clients, rooms):
    room = rooms[event['room_id']]
    for guest in room.guests:
        await connected_clients[guest].send_text(
            str({'type': 'areYouReady', 'data': {}}).replace("'", '"')
        )
    print(f'{event["connectionID"]} - {event["nickname"]} command host Start in room {event["room_id"]}')
    
    timeout_cnt = 0
    while True:
        all_loaded = True
        for guest in room.guests:
            if room.guests[guest].load_complete == 0:
                all_loaded = False
                continue
        
        if all_loaded:
            break
        
        time.sleep(0.1)
        timeout_cnt += 1
        if timeout_cnt > 60:
            print(f'{event["connectionID"]} - {event["nickname"]} command host Start in room {event["room_id"]} timeout')
            return
        
    print(f'{event["connectionID"]} - {event["room_id"]} loading Complition')
    
    for guest in room.guests:
        await connected_clients[guest].send_text(
            str({'type': 'start', 'data': {}}).replace("'", '"')
        )
        