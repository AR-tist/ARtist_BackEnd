async def keyDown(event, connected_clients, rooms):
    if event['room_id'] not in rooms:
        return
    for guest in rooms[event['room_id']].guests:
        if guest != event['connectionID']:
            await connected_clients[guest].send_text(
                str({'type': 'keyDown', 'data': event['data'], 'user_id' : rooms[event['room_id']].guests[event['connectionID']].user_id}).replace("'", '"')
            )

async def keyUp(event, connected_clients, rooms):
    if event['room_id'] not in rooms:
        return
    for guest in rooms[event['room_id']].guests:
        if guest != event['connectionID']:
            await connected_clients[guest].send_text(
               str({'type': 'keyUp', 'data': event['data'], 'user_id' : rooms[event['room_id']].guests[event['connectionID']].user_id}).replace("'", '"')
            )