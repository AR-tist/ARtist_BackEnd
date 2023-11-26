from fastapi import APIRouter, WebSocket
import uuid
import logging
import json
from .multiplay.connect import connect
from .multiplay.disconnect import disconnect
import time

router = APIRouter(
	prefix="/ws",
    tags=["websocket"]
)

connected_clients = {}
rooms = {}


async def message_handler(event):
    if event['type'] == 'connect':
        await connect(event, connected_clients, rooms)
    elif event['type'] == 'disconnect':
        await disconnect(event, connected_clients, rooms)


@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket, filename: str = '', room_id: str = '', nickname: str = '', user_id: str = '', device: str = ''):
    connectionID = str(uuid.uuid4())
    event = {'type': 'connect', 'connectionID': connectionID, 'host': room_id == '', 'filename': filename, 'room_id': room_id, 'nickname': nickname, 'user_id': user_id, 'device': device}
    
    await websocket.accept()
    connected_clients[connectionID] = websocket
    try:
        await message_handler(event)
        while True:
            message = await websocket.receive_text()
            event.update(json.loads(message))
            await message_handler(event)
    except Exception as e:
        if e.__class__.__name__ != 'WebSocketDisconnect':
            print(e)
            logging.error(f'{connectionID} - {e}')
    finally:
        print(f'{connectionID} - {nickname} disconnected')
        event['type'] = 'disconnect'
        await message_handler(event)
        connected_clients[connectionID].close()
        del connected_clients[connectionID]