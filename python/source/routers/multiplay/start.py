async def start(event, rooms):
    room = rooms[event['room_id']]
    
    room.guests[event['connectionID']].load_complete = 1