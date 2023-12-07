async def keyDown(event, connected_clients, rooms):
    if event['room_id'] not in rooms:
        return
    event['data']['user_id'] = rooms[event['room_id']].guests[event['connectionID']].user_id
    for guest in rooms[event['room_id']].guests:
        if guest != event['connectionID']:
            await connected_clients[guest].send_text(
                str({'type': 'keyDown', 'data': event['data']}).replace("'", '"')
            )

async def keyUp(event, connected_clients, rooms):
    if event['room_id'] not in rooms:
        return
    event['data']['user_id'] = rooms[event['room_id']].guests[event['connectionID']].user_id

    for guest in rooms[event['room_id']].guests:
        if guest != event['connectionID']:
            await connected_clients[guest].send_text(
               str({'type': 'keyUp', 'data': event['data']}).replace("'", '"')
            )