from fastapi import FastAPI

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