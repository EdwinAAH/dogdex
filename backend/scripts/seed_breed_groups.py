from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import engine
from app.models.breed_group import BreedGroup


BREED_GROUPS = [
    {
        "name": "Perros de pastor y perros boyeros",
        "description": "Razas tradicionalmente utilizadas para conducir y cuidar ganado.",
    },
    {
        "name": "Pinscher, schnauzer, molosoides y boyeros suizos",
        "description": "Grupo que reúne distintas razas de trabajo y guarda.",
    },
    {
        "name": "Terriers",
        "description": "Razas desarrolladas principalmente para la caza de animales pequeños.",
    },
    {
        "name": "Teckels",
        "description": "Grupo de los dachshunds o perros salchicha.",
    },
    {
        "name": "Spitz y perros de tipo primitivo",
        "description": "Incluye razas como el husky siberiano y el shiba inu.",
    },
    {
        "name": "Sabuesos y perros de rastro",
        "description": "Razas seleccionadas por sus capacidades de rastreo.",
    },
    {
        "name": "Perros de muestra",
        "description": "Razas utilizadas tradicionalmente para localizar y señalar presas.",
    },
    {
        "name": "Perros cobradores, levantadores y de agua",
        "description": "Incluye razas como el labrador retriever y el golden retriever.",
    },
    {
        "name": "Perros de compañía",
        "description": "Razas criadas principalmente para la compañía humana.",
    },
    {
        "name": "Lebreles",
        "description": "Razas como el galgo, tradicionalmente utilizadas para la caza a la vista.",
    },
]


def seed_breed_groups():
    with Session(engine) as db:
        for group_data in BREED_GROUPS:
            existing_group = db.scalar(
                select(BreedGroup).where(
                    BreedGroup.name == group_data["name"]
                )
            )

            if existing_group:
                continue

            db.add(BreedGroup(**group_data))

        db.commit()

    print("Grupos de razas cargados correctamente.")


if __name__ == "__main__":
    seed_breed_groups()