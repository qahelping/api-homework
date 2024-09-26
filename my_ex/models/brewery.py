from typing import Optional, List

from pydantic import BaseModel, Field, field_validator


class BreweryResponse(BaseModel):
    id_: str = Field(alias='id', strict=True)
    name: str = Field(strict=True)
    brewery_type: str = Field(strict=True)
    address_1: str = Field(strict=True)
    address_2: Optional[str] = None
    address_3: Optional[str] = None
    city: str = Field(strict=True)
    state_province: str = Field(strict=True)
    postal_code: str = Field(strict=True)
    country: str = Field(strict=True)
    longitude: str = Field(strict=True)
    latitude: str = Field(strict=True)
    phone: str = Field(strict=True)
    website_url: str = Field(strict=True)
    state: str = Field(strict=True)
    street: str = Field(strict=True)


class MetaResponse(BaseModel):
    total: str = Field(strict=True)
    page: str = Field(strict=True)
    per_page: str = Field(strict=True)
