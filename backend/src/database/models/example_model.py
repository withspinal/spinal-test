from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import Boolean, DateTime, Enum, Text
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from enum import StrEnum
from database.base import Base


class ExampleType(StrEnum):
    EXAMPLE_1 = "example_1"
    EXAMPLE_2 = "example_2"
    EXAMPLE_3 = "example_3"


class ExampleModel(Base):
    __tablename__ = "examples"

    id: Mapped[UUID] = mapped_column(primary_key=True, server_default=func.uuidv7())

    type: Mapped[ExampleType] = mapped_column(Enum(ExampleType), nullable=False)
    col_1: Mapped[str] = mapped_column(Text, nullable=False)
    col_2: Mapped[Optional[str]] = mapped_column(Text, nullable=True)
    active: Mapped[bool] = mapped_column(Boolean, default=True)

    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
