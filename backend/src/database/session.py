import orjson
from typing import Generator

from fastapi import HTTPException
from sqlalchemy import create_engine

from sqlalchemy.exc import IntegrityError

from sqlalchemy.orm import Session, sessionmaker

from settings import get_settings

settings = get_settings()


engine = create_engine(
    settings.database_url,
    echo=False,
    json_serializer=orjson.dumps,
    json_deserializer=orjson.loads,
)


SessionLocal = sessionmaker(
    engine,
    class_=Session,
    expire_on_commit=False,
    autocommit=False,
    autoflush=False,
)


def get_db() -> Generator[Session, None, None]:
    with SessionLocal() as session:
        yield from _session_handler(session)


def _session_handler(session: Session):
    try:
        yield session
        session.commit()
    except IntegrityError as e:
        session.rollback()
        if "unique constraint" in str(e).lower() or "duplicate key" in str(e).lower():
            raise HTTPException(status_code=400, detail="Bad request") from e
        else:
            raise HTTPException(status_code=500, detail="Internal error") from e
    except Exception as e:
        session.rollback()
        raise e
