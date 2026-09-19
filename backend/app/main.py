from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.db.session import check_database_connection, get_db
from app.repositories.country_repository import get_all_countries
from app.schemas.country import CountryResponse
from app.repositories.breed_repository import get_all_breeds
from app.schemas.breed import BreedResponse, BreedListResponse
from fastapi import HTTPException, Query
from app.repositories.breed_repository import get_breed_by_slug
from typing import Optional
from pathlib import Path
from fastapi.staticfiles import StaticFiles

app = FastAPI(
    title="DogDex API",
    description="API para explorar y comparar razas de perros",
    version="0.1.0",
)


# Directorio raíz del backend
BACKEND_DIR = Path(__file__).resolve().parent.parent

# Permitir que FastAPI sirva las fotografías
app.mount(
    "/static",
    StaticFiles(directory=BACKEND_DIR / "static"),
    name="static",
)


@app.get("/")
def root():
    return {
        "message": "DogDex API",
        "status": "running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "ok"
    }

@app.get("/health/db")
def database_health_check():
    database_name = check_database_connection()

    return {
        "status": "Database connection is healthy",
        "database": database_name
    }

@app.get("/countries", response_model=list[CountryResponse])
def get_countries(db: Session = Depends(get_db)):
    return get_all_countries(db)

@app.get("/breeds", response_model=BreedListResponse)
def list_breeds(
    search: Optional[str] = None,
    country: Optional[str] = None,
    group: Optional[int] = None,
    size: Optional[str] = None,
    limit: int = Query(default=20, ge=1, le=100),
    offset: int = Query(default=0, ge=0),
    db: Session = Depends(get_db),
):
    return get_all_breeds(
        db,
        search=search,
        country=country,
        group=group,
        size=size,
        limit=limit,
        offset=offset,
    )

@app.get("/breeds/{slug}", response_model=BreedResponse)
def get_breed_detail(
    slug: str,
    db: Session = Depends(get_db),
):
    breed = get_breed_by_slug(db, slug)

    if breed is None:
        raise HTTPException(
            status_code=404,
            detail="Raza no encontrada",
        )

    return breed