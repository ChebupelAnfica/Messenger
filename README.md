Установка и запуск

Клонируйте репозиторий:

git clone https://github.com/yourusername/chat-app.git
cd chat-app

Соберите и запустите контейнеры:

docker-compose up --build

Приложение будет доступно по адресу:

API: http://127.0.0.1:8000

Swagger UI: http://127.0.0.1:8000/docs

API

GET /history/{chat_id}

Получить историю сообщений по ID чата.

Пример:

curl -X 'GET' 'http://127.0.0.1:8000/history/1?limit=5&offset=0'

Ответ:

[
  {
    "id": 1,
    "chat_id": 1,
    "sender_id": 1,
    "text": "Привет!",
    "timestamp": "2025-04-04T10:30:00",
    "read": true
  },
  ...
]

Тестирование

Запустите тесты:

pytest

docker-compose exec app bash -c "PYTHONPATH=/app pytest /app/tests/test_main.py"

Создание тестовых данных

Для создания тестовых данных используйте следующий скрипт:

python create_test_data.py

Особенности

WebSocket:

Подключение через WebSocket для обмена сообщениями в реальном времени.

Сообщения сохраняются в базе данных.

Реализована обработка статуса "прочитано".

Контейнеризация:

Приложение работает через Docker и Docker Compose.

Запуск всех компонентов через docker-compose up.