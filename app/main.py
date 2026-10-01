from fastapi import FastAPI, HTTPException, status

from app.schemas import StationCreate, StationOut

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
