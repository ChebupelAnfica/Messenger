from fastapi import FastAPI, Security, Depends, HTTPException, status
from app.routes import router as message_router
from fastapi import WebSocket, WebSocketDisconnect
from app.websocket import websocket_endpoint
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta

app = FastAPI()

app.include_router(message_router)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class UserLogin(BaseModel):
    username: str
    password: str


@app.websocket("/ws/chat/{chat_id}")
async def websocket_chat(websocket: WebSocket, chat_id: int):
    await websocket_endpoint(websocket, chat_id)


@app.get("/protected")
async def protected_route(token: str = Depends(oauth2_scheme)):
    # Проверка токена и извлечение пользователя
    return {"message": "This is a protected route"}


@app.post("/token")
async def login_for_access_token(form_data: UserLogin):
    if form_data.username == "test" and form_data.password == "password":  # Проверь тут с базой данных
        access_token = create_access_token(data={"sub": form_data.username})
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, "SECRET_KEY", algorithm="HS256")
    return encoded_jwt


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, "SECRET_KEY", algorithms=["HS256"])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username


@app.get("/protected")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Hello {current_user}, you are authorized!"}
