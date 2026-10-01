from fastapi import Depends, FastAPI, HTTPException, status
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import models
from app.db import Base, engine, get_db
from app.schemas import StationCreate, StationOut, StationStatus, StationUpdate

app = FastAPI(title="Stations de vélos", version="0.1.0")
Base.metadata.create_all(bind=engine)


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check() -> dict[str, str]:
    return {"status": "ok"}


@app.post(
    "/stations",
    response_model=StationOut,
    status_code=status.HTTP_201_CREATED,
)
def create_station(
    data: StationCreate, db: Session = Depends(get_db)
) -> models.Station:
    station = models.Station(**data.model_dump())
    db.add(station)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Station code '{data.code}' already exists",
        )
    db.refresh(station)
    return station


@app.get("/stations", response_model=list[StationOut])
def list_stations(
    status: StationStatus | None = None, db: Session = Depends(get_db)
) -> list[models.Station]:
    query = select(models.Station).order_by(models.Station.id)
    if status is not None:
        query = query.where(models.Station.status == status)
    return list(db.scalars(query))


@app.get("/stations/{station_id}", response_model=StationOut)
def get_station(station_id: int, db: Session = Depends(get_db)) -> models.Station:
    return find_station(db, station_id)


def find_station(db: Session, station_id: int) -> models.Station:
    station = db.get(models.Station, station_id)
    if station is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Station {station_id} not found",
        )
    return station


@app.patch("/stations/{station_id}", response_model=StationOut)
def update_station(
    station_id: int, data: StationUpdate, db: Session = Depends(get_db)
) -> models.Station:
    station = find_station(db, station_id)
    updates = data.model_dump(exclude_unset=True, exclude_none=True)
    for field, value in updates.items():
        setattr(station, field, value)
    db.commit()
    db.refresh(station)
    return station
