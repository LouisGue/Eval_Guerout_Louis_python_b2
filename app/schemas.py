from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

StationStatus = Literal["open", "closed", "maintenance"]


class StationCreate(BaseModel):
    model_config = ConfigDict(str_strip_whitespace=True)
    code: str = Field(min_length=1)
    name: str = Field(min_length=1)
    capacity: int = Field(ge=1)
    status: StationStatus = "open"


class StationOut(StationCreate):
    id: int
