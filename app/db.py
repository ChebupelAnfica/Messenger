import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
# Чтение DATABASE_URL из переменной окружения
DATABASE_URL = os.getenv("DATABASE_URL") + "?client_encoding=utf8"
if DATABASE_URL is None:
    raise ValueError("DATABASE_URL environment variable is not set")

# Заменяем "postgresql://" на "postgresql+asyncpg://", чтобы использовать асинхронный драйвер
DATABASE_URL = DATABASE_URL.replace("postgresql://", "postgresql+asyncpg://")

# Создаем асинхронный движок для SQLAlchemy
engine = create_engine(DATABASE_URL)
# Настройка сессии для работы с базой данных
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для декларативных моделей
Base = declarative_base()


# Функция для получения сессии
async def get_db():
    async with SessionLocal() as session:
        yield session


try:
    with engine.connect() as connection:
        print("Подключение к базе данных успешно!")
except Exception as e:
    print(f"Ошибка подключения: {e}")