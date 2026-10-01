from fastapi import FastAPI, status

from app.schemas import StationCreate

app = FastAPI(title="Dock Control", version="0.1.0")


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/stations", status_code=status.HTTP_201_CREATED)
def create_station(station: StationCreate):
    return station
