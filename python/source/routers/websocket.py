from fastapi import APIRouter, WebSocket
import uuid
import logging
import json
from .multiplay.connect import connect
import time

router = APIRouter(
	prefix="/ws",
    tags=["websocket"]
)

connected_clients = {}

async def message_handler(event):
    if event['type'] == 'connect':
        connect(event, connected_clients)
    if event['type'] == 'disconnect':
        pass
    if event['type'] == 'message':
        for connection_id in connected_clients:
            if connection_id != event['connection_id']:
                await connected_clients[connection_id].send_text(event['message'])


@router.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    connection_id = str(uuid.uuid4())
    connected_clients[connection_id] = websocket
    try:
        message_handler({'type': 'connect', 'connection_id': connection_id})
        while True:
            message = await websocket.receive_text()
            event = json.loads(message)
            event['connection_id'] = connection_id
            await message_handler(event)
    except Exception as e:
        logging.error(f'{connection_id} - {e}')
    finally:
        message_handler({'type': 'disconnect', 'connection_id': connection_id})
        del connected_clients[connection_id]