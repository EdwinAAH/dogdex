import uuid

from sqlalchemy import ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class BreedCoatType(Base):
    __tablename__ = "breed_coat_type"

    breed_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("breed.id", ondelete="CASCADE"),
        primary_key=True,
    )

    coat_type_id: Mapped[int] = mapped_column(
        ForeignKey("coat_type.id", ondelete="CASCADE"),
        primary_key=True,
    )