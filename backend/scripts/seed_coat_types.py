from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import engine
from app.models.coat_type import CoatType


COAT_TYPES = [
    {
        "name": "Corto",
        "description": "Pelaje de longitud corta, generalmente pegado al cuerpo.",
    },
    {
        "name": "Largo",
        "description": "Pelaje de longitud considerable.",
    },
    {
        "name": "Medio",
        "description": "Pelaje de longitud intermedia.",
    },
    {
        "name": "Rizado",
        "description": "Pelaje que forma rizos u ondas pronunciadas.",
    },
    {
        "name": "Duro",
        "description": "Pelaje de textura áspera o rígida.",
    },
    {
        "name": "Liso",
        "description": "Pelaje de textura lisa.",
    },
    {
        "name": "Doble capa",
        "description": "Pelaje compuesto por una capa externa y una capa interna.",
    },
    {
        "name": "Sin pelo",
        "description": "Ausencia total o parcial de pelaje.",
    },
    {
        "name": "Cordado",
        "description": "Pelaje que forma cordones de pelo.",
    },
]


def seed_coat_types():
    with Session(engine) as db:
        for coat_data in COAT_TYPES:
            existing_coat = db.scalar(
                select(CoatType).where(
                    CoatType.name == coat_data["name"]
                )
            )

            if existing_coat:
                continue

            db.add(CoatType(**coat_data))

        db.commit()

    print("Tipos de pelaje cargados correctamente.")


if __name__ == "__main__":
    seed_coat_types()