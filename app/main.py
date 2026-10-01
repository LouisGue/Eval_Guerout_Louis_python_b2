from fastapi import FastAPI, HTTPException, status

from app.schemas import StationCreate, StationOut, StationStatus, StationUpdate

app = FastAPI(title="Dock Control", version="0.1.0")


@app.get("/health", status_code=status.HTTP_200_OK)
def health_check() -> dict[str, str]:
    return {"status": "ok"}


stations: list[StationOut] = []
next_id = 1


@app.post(
    "/stations",
    response_model=StationOut,
    status_code=status.HTTP_201_CREATED,
)
def create_station(data: StationCreate) -> StationOut:
    global next_id

    if any(s.code == data.code for s in stations):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Station code '{data.code}' already exists",
        )

    station = StationOut(id=next_id, **data.model_dump())
    stations.append(station)
    next_id += 1
    return station


@app.get("/stations", response_model=list[StationOut])
def list_stations(status: StationStatus | None = None) -> list[StationOut]:
    if status is None:
        return stations
    return [s for s in stations if s.status == status]


@app.get("/stations/{station_id}", response_model=StationOut)
def get_station(station_id: int) -> StationOut:
    return find_station(station_id)


def find_station(station_id: int) -> StationOut:
    for station in stations:
        if station.id == station_id:
            return station
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Station {station_id} not found",
    )


@app.patch("/stations/{station_id}", response_model=StationOut)
def update_station(station_id: int, data: StationUpdate) -> StationOut:
    station = find_station(station_id)
    updates = data.model_dump(exclude_unset=True, exclude_none=True)
    for field, value in updates.items():
        setattr(station, field, value)
    return station
