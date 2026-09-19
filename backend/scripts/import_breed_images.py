
import json
from pathlib import Path

from sqlalchemy import select, update
from sqlalchemy.orm import Session

from app.db.session import engine
from app.models.breed import Breed
from app.models.breed_image import BreedImage


BACKEND_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BACKEND_DIR / "data" / "breed_images.json"


def import_breed_images():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        images_data = json.load(file)

    with Session(engine) as db:
        for image_data in images_data:
            slug = image_data["breed_slug"]
            image_url = image_data["image_url"]

            # Comprobar que el archivo local existe
            local_path = BACKEND_DIR / image_url.lstrip("/")

            if not local_path.is_file():
                raise FileNotFoundError(
                    f"No existe la imagen: {local_path}"
                )

            # Buscar la raza mediante su slug
            breed = db.scalar(
                select(Breed).where(Breed.slug == slug)
            )

            if breed is None:
                raise ValueError(
                    f"No existe la raza: {slug}"
                )

            # Buscar si esta imagen ya fue registrada
            existing_image = db.scalar(
                select(BreedImage).where(
                    BreedImage.breed_id == breed.id,
                    BreedImage.image_url == image_url,
                )
            )

            # Si será la principal, desmarcar las anteriores
            if image_data["is_primary"]:
                db.execute(
                    update(BreedImage)
                    .where(BreedImage.breed_id == breed.id)
                    .values(is_primary=False)
                )

            image_fields = {
                key: value
                for key, value in image_data.items()
                if key != "breed_slug"
            }

            if existing_image:
                for field, value in image_fields.items():
                    setattr(existing_image, field, value)

                print(f"Actualizada imagen: {slug}")

            else:
                image = BreedImage(
                    breed_id=breed.id,
                    **image_fields,
                )

                db.add(image)

                print(f"Creada imagen: {slug}")

        db.commit()

    print("Importación de imágenes finalizada.")


if __name__ == "__main__":
    import_breed_images()