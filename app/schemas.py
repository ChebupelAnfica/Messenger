from pydantic import BaseModel
from datetime import datetime
from typing import Optional


# Схема для чатов
class ChatBase(BaseModel):
    name: str
    type: str  # 'personal' или 'group'


class ChatCreate(ChatBase):
    pass


class Chat(ChatBase):
    id: int

    class Config:
        orm_mode = True


# Схема для сообщений
class MessageBase(BaseModel):
    chat_id: int
    sender_id: int
    text: str


class MessageCreate(MessageBase):
    pass


class Message(MessageBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True
