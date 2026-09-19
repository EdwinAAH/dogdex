import uuid
from datetime import datetime
from typing import Optional

from sqlalchemy import (
    CheckConstraint,
    DateTime,
    Float,
    ForeignKey,
    SmallInteger,
    String,
    Text,
    func,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base
from app.models.country import Country
from app.models.breed_group import BreedGroup
from app.models.coat_type import CoatType


class Breed(Base):
    __tablename__ = "breed"

    # Identidad
    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    slug: Mapped[str] = mapped_column(
        String(180),
        unique=True,
        nullable=False,
    )

    # Clasificación
    country_id: Mapped[int] = mapped_column(
        ForeignKey("country.id"),
        nullable=False,
    )

    group_id: Mapped[int] = mapped_column(
        ForeignKey("breed_group.id"),
        nullable=False,
    )

    # Relaciones con los catálogos
    country: Mapped[Country] = relationship("Country")

    group: Mapped[BreedGroup] = relationship("BreedGroup")

    coat_types: Mapped[list[CoatType]] = relationship(
        "CoatType",
        secondary="breed_coat_type",
    )

    # Características físicas
    male_height_min_cm: Mapped[Optional[float]] = mapped_column(Float)
    male_height_max_cm: Mapped[Optional[float]] = mapped_column(Float)

    female_height_min_cm: Mapped[Optional[float]] = mapped_column(Float)
    female_height_max_cm: Mapped[Optional[float]] = mapped_column(Float)

    male_weight_min_kg: Mapped[Optional[float]] = mapped_column(Float)
    male_weight_max_kg: Mapped[Optional[float]] = mapped_column(Float)

    female_weight_min_kg: Mapped[Optional[float]] = mapped_column(Float)
    female_weight_max_kg: Mapped[Optional[float]] = mapped_column(Float)

    lifespan_min_years: Mapped[Optional[int]] = mapped_column(SmallInteger)
    lifespan_max_years: Mapped[Optional[int]] = mapped_column(SmallInteger)

    size_category: Mapped[Optional[str]] = mapped_column(
        String(20),
    )

    # Información descriptiva
    original_purpose: Mapped[Optional[str]] = mapped_column(Text)
    description: Mapped[Optional[str]] = mapped_column(Text)
    history: Mapped[Optional[str]] = mapped_column(Text)

    # Auditoría
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    __table_args__ = (
        CheckConstraint(
            "size_category IS NULL OR "
            "size_category IN ('small', 'medium', 'large', 'giant')",
            name="ck_breed_size_category",
        ),
    )