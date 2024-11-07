import asyncio
import websockets
import json
import os
from dotenv import load_dotenv

class RealtimeServer:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.openai_ws = None
        self.clients = set()  # 存储客户端连接
        
    async def handle_client(self, websocket, path):
        """处理客户端连接"""
        try:
            # 将新客户端添加到集合中
            self.clients.add(websocket)
            
            # 如果没有 OpenAI 连接，建立连接
            if not self.openai_ws:
                await self.connect_to_openai()
            
            # 处理客户端消息
            async for message in websocket:
                # 转发到 OpenAI
                await self.openai_ws.send(message)
                
        except Exception as e:
            print(f"Error handling client: {e}")
        finally:
            self.clients.remove(websocket)
            
    async def connect_to_openai(self):
        """连接到 OpenAI 服务器"""
        url = "wss://api.openai.com/v1/realtime?model=gpt-4o-realtime-preview-2024-10-01"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "OpenAI-Beta": "realtime=v1"
        }
        
        self.openai_ws = await websockets.connect(url, extra_headers=headers)
        # 启动 OpenAI 响应处理
        asyncio.create_task(self.handle_openai_messages())
        
    async def handle_openai_messages(self):
        """处理来自 OpenAI 的消息"""
        try:
            async for message in self.openai_ws:
                # 广播给所有连接的客户端
                for client in self.clients:
                    await client.send(message)
        except Exception as e:
            print(f"Error from OpenAI connection: {e}")
            # 实现重连逻辑
            await self.reconnect_to_openai()
            
    async def reconnect_to_openai(self):
        """重新连接到 OpenAI"""
        try:
            if self.openai_ws:
                await self.openai_ws.close()
            await self.connect_to_openai()
        except Exception as e:
            print(f"Reconnection failed: {e}")

    async def start_server(self, host='localhost', port=8765):
        """启动服务器"""
        async with websockets.serve(self.handle_client, host, port):
            print(f"Server started on ws://{host}:{port}")
            await asyncio.Future()  # 保持服务器运行 