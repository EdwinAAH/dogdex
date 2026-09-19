from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict, field_validator

class CountryInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class BreedGroupInfo(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str

class BreedResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID
    name: str
    slug: str

    country_id: int
    group_id: int
    country: CountryInfo
    group: BreedGroupInfo
    coat_types: list[str]

    male_height_min_cm: Optional[float] = None
    male_height_max_cm: Optional[float] = None
    female_height_min_cm: Optional[float] = None
    female_height_max_cm: Optional[float] = None

    male_weight_min_kg: Optional[float] = None
    male_weight_max_kg: Optional[float] = None
    female_weight_min_kg: Optional[float] = None
    female_weight_max_kg: Optional[float] = None

    lifespan_min_years: Optional[int] = None
    lifespan_max_years: Optional[int] = None

    size_category: Optional[str] = None
    original_purpose: Optional[str] = None
    description: Optional[str] = None
    history: Optional[str] = None

    created_at: datetime
    updated_at: datetime

    @field_validator("coat_types", mode="before")
    @classmethod
    def convert_coat_types(cls, value):
        return sorted(coat.name for coat in value)

    
class BreedListResponse(BaseModel):
    total: int
    limit: int
    offset: int
    items: list[BreedResponse]