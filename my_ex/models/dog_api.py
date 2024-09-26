from typing import List

from pydantic import BaseModel, Field, field_validator


class DogApiResponse(BaseModel):
    message: str = Field(strict=True)
    status: str = Field(strict=True)

    @field_validator("status")
    @classmethod
    def status_must_be_success(cls, value: str):
        if value not in ["success", "error"]:
            raise ValueError(f"Status is not [success, error], but given {value}")
        return value



class DogApiListResponse(BaseModel):
    message: List = Field(strict=True)
    status: str = Field(strict=True)
