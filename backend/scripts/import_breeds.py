
import json
from pathlib import Path

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.db.session import engine
from app.models.breed import Breed
from app.models.breed_coat_type import BreedCoatType
from app.models.breed_group import BreedGroup
from app.models.coat_type import CoatType
from app.models.country import Country


DATA_FILE = Path(__file__).resolve().parent.parent / "data" / "breeds.json"


def import_breeds():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        breeds_data = json.load(file)

    with Session(engine) as db:
        for breed_data in breeds_data:
            slug = breed_data["slug"]

            # Evitar duplicados
            existing_breed = db.scalar(
                select(Breed).where(Breed.slug == slug)
            )


            # Resolver país
            country = db.scalar(
                select(Country).where(
                    Country.iso_code == breed_data["country_iso"]
                )
            )

            # Resolver grupo
            group = db.scalar(
                select(BreedGroup).where(
                    BreedGroup.name == breed_data["group_name"]
                )
            )

            # Resolver pelajes
            coat_names = breed_data.get("coat_types", [])

            coat_types = db.scalars(
                select(CoatType).where(
                    CoatType.name.in_(coat_names)
                )
            ).all()

            if country is None or group is None:
                raise ValueError(
                    f"País o grupo no encontrado para {slug}"
                )

            if len(coat_types) != len(set(coat_names)):
                raise ValueError(
                    f"Algún tipo de pelaje no existe para {slug}"
                )


            # Separar los campos propios de Breed
            breed_fields = {
                key: value
                for key, value in breed_data.items()
                if key not in ("country_iso", "group_name", "coat_types")
            }

            if existing_breed:
                # Actualizar la raza sin cambiar su UUID
                breed = existing_breed

                for field, value in breed_fields.items():
                    setattr(breed, field, value)

                breed.country_id = country.id
                breed.group_id = group.id

                # Eliminar asociaciones anteriores de pelaje
                previous_coats = db.scalars(
                    select(BreedCoatType).where(
                        BreedCoatType.breed_id == breed.id
                    )
                ).all()

                for previous_coat in previous_coats:
                    db.delete(previous_coat)

                db.flush()

                action = "Actualizada"

            else:
                # Crear una raza nueva
                breed = Breed(
                    **breed_fields,
                    country_id=country.id,
                    group_id=group.id,
                )

                db.add(breed)
                db.flush()

                action = "Creada"

            # Registrar los pelajes definidos en el JSON
            for coat_type in coat_types:
                db.add(
                    BreedCoatType(
                        breed_id=breed.id,
                        coat_type_id=coat_type.id,
                    )
                )

            print(f"{action}: {breed.name}")

        db.commit()

    print("Importación finalizada.")


if __name__ == "__main__":
    import_breeds()