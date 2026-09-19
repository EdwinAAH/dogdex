from sqlalchemy import select, func
from sqlalchemy.orm import Session, selectinload
from app.models.breed import Breed
from typing import Optional




def get_all_breeds(
    db: Session,
    search: Optional[str] = None,
    country: Optional[str] = None,
    group: Optional[int] = None,
    size: Optional[str] = None,
    limit: int = 20,
    offset: int = 0,
):
    statement = (
        select(Breed)
        .options(
            selectinload(Breed.country),
            selectinload(Breed.group),
            selectinload(Breed.coat_types),
        )
    )

    if search:
        statement = statement.where(
            Breed.name.ilike(f"%{search}%")
        )

    if country:
        statement = statement.where(
            Breed.country.has(iso_code=country.upper())
        )

    if group is not None:
        statement = statement.where(
            Breed.group_id == group
        )

    if size:
        statement = statement.where(
            Breed.size_category == size
        )

    
    # Contar todas las razas que cumplen los filtros
    count_statement = (
        statement
        .with_only_columns(func.count(Breed.id))
        .order_by(None)
    )

    total = db.scalar(count_statement) or 0

    statement = (
        statement
        .order_by(Breed.name, Breed.id)
        .offset(offset)
        .limit(limit)
    )

    breeds = db.scalars(statement).all()

    return {
        "total": total,
        "limit": limit,
        "offset": offset,
        "items": breeds,
    }


def get_breed_by_slug(db: Session, slug: str):
    statement = (
        select(Breed)
        .options(
            selectinload(Breed.country),
            selectinload(Breed.group),
            selectinload(Breed.coat_types),
        )
        .where(Breed.slug == slug)
    )

    return db.scalar(statement)