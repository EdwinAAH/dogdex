from typing import Optional

from pydantic import BaseModel, ConfigDict


class CountryResponse(BaseModel):
    id: int
    name: str
    iso_code: str
    continent: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    model_config = ConfigDict(from_attributes=True)