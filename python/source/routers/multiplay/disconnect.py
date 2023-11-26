import logging


async def disconnect(event, connected_clients, rooms):
    room = rooms[event['room_id']]
    del room.guests[event['connectionID']]

    logging.info(f'{event["connectionID"]} - {event["nickname"]} left room {event["room_id"]}')
    if len(room.guests) == 0:
        del rooms[event['room_id']]
        logging.info(f'Room {event["room_id"]} deleted')

    if event['host']:
        tmp_guests = room.guests.copy()
        for guest in tmp_guests:
            await connected_clients[guest].close()

        
