import logging
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(
os.path.abspath(os.path.dirname(__file__))))))

from models.Room import Room
from models.Music import Music
from models.Client import Client
from db.get_midi import get_midi

import uuid

async def connect(event, connected_clients, rooms):
    if event['host']:
        music_document = get_midi(event['filename'])
        client = Client(connectionID=event['connectionID'],
                        nickname=event['nickname'],
                        user_id=event['user_id'],
                        device=event['device'],
                        host=1,
                        load_complete=0,
                        )
        room = Room(room_id=str(uuid.uuid4()),
                    host_nickname = client.nickname,
                    host_id=event['user_id'],
                    music_instance=Music(music_document),
                    guests={
                        client.connectionID: client
                        },
                    )
        event['room_id'] = room.room_id
        rooms[room.room_id] = room

        await connected_clients[event['connectionID']].send_text(
            str({'type': 'connect','data' :room.to_dict()}).replace("'", '"')
        )
        print(f'{event["connectionID"]} - {event["nickname"]} created room {event["room_id"]}')
    else:
        room = rooms[event['room_id']]
        client = Client(connectionID=event['connectionID'],
                        nickname=event['nickname'],
                        user_id=event['user_id'],
                        device=event['device'],
                        host=0,
                        load_complete=0,
                        )
        room.guests[client.connectionID] = client
        await connected_clients[event['connectionID']].send_text(
            str({'type': 'connect','data' :room.to_dict()}).replace("'", '"')
        )
        print(f'{event["connectionID"]} - {event["nickname"]} joined room {event["room_id"]}')
    
        for guest in room.guests:
            if guest != event['connectionID']:
                await connected_clients[guest].send_text(
                    str({'type': 'join', 'data': room.to_dict()}).replace("'", '"')
                )


