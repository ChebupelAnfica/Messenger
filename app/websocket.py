from fastapi import WebSocket, WebSocketDisconnect
from app.db import SessionLocal
from app.models import Message, Chat
from sqlalchemy.orm import Session


class ChatConnectionManager:
    def __init__(self):
        self.active_connections: dict[int, WebSocket] = {}

    async def connect(self, websocket: WebSocket, chat_id: int):
        await websocket.accept()
        self.active_connections[chat_id] = websocket

    async def disconnect(self, chat_id: int):
        if chat_id in self.active_connections:
            del self.active_connections[chat_id]

    async def send_message(self, chat_id: int, message: str):
        if chat_id in self.active_connections:
            websocket = self.active_connections[chat_id]
            await websocket.send_text(message)


manager = ChatConnectionManager()


async def websocket_endpoint(websocket: WebSocket, chat_id: int):
    await manager.connect(websocket, chat_id)
    try:
        while True:
            message = await websocket.receive_text()

            # Проверка на дублирование
            db: Session = SessionLocal()
            existing_message = db.query(Message).filter_by(chat_id=chat_id, sender_id=1, text=message).first()

            if existing_message:
                await websocket.send_text("Duplicate message detected")
                continue

            new_message = Message(chat_id=chat_id, sender_id=1, text=message)
            db.add(new_message)
            db.commit()
            db.refresh(new_message)
            await manager.send_message(chat_id, message)
    except WebSocketDisconnect:
        await manager.disconnect(chat_id)
