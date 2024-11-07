import asyncio
import websockets
import json

class RealtimeClient:
    def __init__(self, server_url="ws://localhost:8765"):
        self.server_url = server_url
        self.ws = None
        
    async def connect(self):
        """连接到应用服务器"""
        self.ws = await websockets.connect(self.server_url)
        
    async def send_message(self, text):
        """发送消息"""
        message = {
            "type": "conversation.item.create",
            "item": {
                "type": "message",
                "role": "user",
                "content": [{
                    "type": "input_text",
                    "text": text
                }]
            }
        }
        await self.ws.send(json.dumps(message))
        
    async def receive_messages(self):
        """接收服务器消息"""
        async for message in self.ws:
            event = json.loads(message)
            if event['type'] == 'response.text.delta':
                print(f"收到回复: {event['delta']}") 