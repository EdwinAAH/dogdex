
import uuid
from typing import Optional

from sqlalchemy import Boolean, ForeignKey, String, Text, text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base


class BreedImage(Base):
    __tablename__ = "breed_image"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
    )

    breed_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("breed.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    image_url: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    source_url: Mapped[Optional[str]] = mapped_column(Text)

    author: Mapped[Optional[str]] = mapped_column(String(200))

    license: Mapped[Optional[str]] = mapped_column(String(100))

    alt_text: Mapped[str] = mapped_column(
        String(250),
        nullable=False,
    )

    is_primary: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        server_default=text("false"),
    )