from sqlalchemy import String, Float
from sqlalchemy.orm import Mapped, mapped_column
from typing import Optional

from app.models.base import Base


class Country(Base):
    __tablename__ = "country"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    iso_code: Mapped[str] = mapped_column(
        String(2),
        unique=True,
        nullable=False,
    )

    continent: Mapped[Optional[str]] = mapped_column(
        String(50),
        nullable=True,
    )

    latitude: Mapped[Optional[float]] = mapped_column(
        Float,
        nullable=True,
    )

    longitude: Mapped[Optional[float]] = mapped_column(
        Float,
        nullable=True,
    )