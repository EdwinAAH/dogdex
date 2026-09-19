from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.country import Country


def get_all_countries(db: Session):
    statement = select(Country).order_by(Country.name)

    return db.scalars(statement).all()