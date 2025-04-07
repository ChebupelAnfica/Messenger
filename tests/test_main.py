from fastapi.testclient import TestClient
from app.main import app  # Импортируем приложение FastAPI

client = TestClient(app)


def test_login():
    # Отправляем запрос для получения токена
    response = client.post(
        "/token", json={"username": "test", "password": "password"}
    )

    # Проверяем, что статус ответа - 200
    assert response.status_code == 200

    # Проверяем, что в ответе есть поле 'access_token'
    assert "access_token" in response.json()

    # Проверка на наличие типа токена
    assert response.json()["token_type"] == "bearer"


def test_protected_route():
    # Получаем токен с правильными данными для входа
    response = client.post(
        "/token", json={"username": "test", "password": "password"}
    )
    token = response.json().get("access_token")

    # Отправляем запрос к защищённому маршруту с токеном в заголовке
    headers = {"Authorization": f"Bearer {token}"}
    protected_response = client.get("/protected", headers=headers)

    # Проверяем, что статус ответа - 200
    assert protected_response.status_code == 200

    # Проверяем, что в ответе есть поле "message"
    assert "message" in protected_response.json()


def test_get_messages():
    # Отправляем запрос с пагинацией
    response = client.get("/messages/1?limit=5&offset=0")  # Этот запрос передает параметры limit и offset

    # Проверяем, что статус ответа - 200
    assert response.status_code == 200

    # Проверяем, что в ответе не более 5 сообщений
    assert len(response.json()) <= 5
