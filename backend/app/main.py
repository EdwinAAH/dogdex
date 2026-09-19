from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.db.session import check_database_connection, get_db
from app.repositories.country_repository import get_all_countries
from app.schemas.country import CountryResponse

app = FastAPI(
    title="DogDex API",
    description="API para explorar y comparar razas de perros",
    version="0.1.0",
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