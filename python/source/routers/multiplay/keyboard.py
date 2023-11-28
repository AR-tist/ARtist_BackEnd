async def keyDown(event, connected_clients, rooms):
    if event['room_id'] not in rooms:
        return
    for connectionID in rooms[event['room_id']]:
        if connectionID != event['connectionID']:
            await connected_clients[connectionID].send_text(
                str({'type': 'keyDown', 'data': event['data']}).replace("'", '"'))
            
async def keyUp(event, connected_clients, rooms):
    if event['room_id'] not in rooms:
        return
    for connectionID in rooms[event['room_id']]:
        if connectionID != event['connectionID']:
            await connected_clients[connectionID].send_text(
                str({'type': 'keyUp', 'data': event['data']}).replace("'", '"'))
            
