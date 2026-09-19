import os

from dotenv import load_dotenv
from sqlalchemy import create_engine, text

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL no está configurada")

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def check_database_connection():
    with engine.connect() as connection:
        result = connection.execute(
            text("SELECT current_database()")
        )

        return result.scalar_one()