from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Chat, Message
from app.schemas import ChatCreate, MessageCreate, Chat, Message

router = APIRouter()


# Получить список чатов
@router.get("/chats", response_model=list[Chat])
def get_chats(db: Session = Depends(SessionLocal)):
    chats = db.query(Chat).all()
    return chats


# Создать новый чат
@router.post("/chats", response_model=Chat)
def create_chat(chat: ChatCreate, db: Session = Depends(SessionLocal)):
    new_chat = Chat(name=chat.name, type=chat.type)
    db.add(new_chat)
    db.commit()
    db.refresh(new_chat)
    return new_chat


# Получить список сообщений для чата
@router.get("/messages/{chat_id}", response_model=list[Message])
def get_messages(chat_id: int, limit: int = 10, offset: int = 0, db: Session = Depends(SessionLocal)):
    messages = db.query(Message).filter(Message.chat_id == chat_id).limit(limit).offset(offset).all()
    return messages


# Создать новое сообщение
@router.post("/messages", response_model=Message)
def create_message(message: MessageCreate, db: Session = Depends(SessionLocal)):
    new_message = Message(chat_id=message.chat_id, sender_id=message.sender_id, text=message.text)
    db.add(new_message)
    db.commit()
    db.refresh(new_message)
    return new_message
