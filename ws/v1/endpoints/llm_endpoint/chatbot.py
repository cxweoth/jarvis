from fastapi import APIRouter, WebSocket
from starlette.websockets import WebSocketState
from model.ai_agents import LlamaAgent
import time

from cfg import Config

router = APIRouter()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        llama_agent = LlamaAgent()
        while True:
            data = await websocket.receive_text()
            print('Received:', data)
            stime = time.time()
            reply = llama_agent.get_reply(data)
            etime = time.time()
            print('Reply:', reply, 'with time:', etime - stime)
            await websocket.send_text(f"{reply}")
    except Exception as e:
        print('Error:', e)
    finally:
        try:
            await websocket.close()
        except Exception as e:
            print('Close web socket error:', e)
