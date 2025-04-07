from sqlalchemy import create_engine, StaticPool
from sqlalchemy.orm import sessionmaker
from alembic import context
from app.models import Base, User, Chat, Message  # Импортируем твой Base, если нужно
import os
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy import create_engine


DATABASE_URL = os.getenv("DATABASE_URL")
# Создаем синхронное подключение через psycopg2

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def run_migrations_offline():
    context.configure(
        url=DATABASE_URL,
        target_metadata=Base.metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    connectable = engine.connect()  # Используем синхронное соединение
    with connectable.begin():
        context.configure(
            connection=connectable,
            target_metadata=Base.metadata,
        )
        with context.begin_transaction():
            context.run_migrations()