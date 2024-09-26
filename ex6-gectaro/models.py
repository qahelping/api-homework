from pydantic import BaseModel, Field, field_validator, ConfigDict
from typing import Optional, List
from datetime import datetime


class PostResourceRequests(BaseModel):
    model_config = ConfigDict(extra="allow")
    project_tasks_resource_id: int
    needed_at: int
    volume: int
    is_over_budget: Optional[int] = 0


class PostProjectTaskResource(BaseModel):
    model_config = ConfigDict(extra="allow")
    name: str
    needed_at: int
    project_id: int
    type: int
    volume: int


class GetResourceRequestsId(BaseModel):
    id_: int = Field(alias="id", strict=True)
    project_tasks_resource_id: int
    volume: float
    cost: float
    batch_number: Optional[int] = None
    batch_parent_request_id: Optional[int] = None
    is_over_budget: bool
    created_at: int
    updated_at: int
    user_id: int
    needed_at: int
    created_by: int

    # метод класса, чтобы проверка шла до инициализации объекта
    @field_validator("created_at", "updated_at", check_fields=True)
    @classmethod
    def datetime_must_be_in_past(cls, value: int):
        dt = datetime.utcfromtimestamp(value)
        if dt >= datetime.utcnow():
            raise ValueError("Datetime must be in the past")
        return value

    @field_validator("id_")
    @classmethod
    def id_must_be_7_chars(cls, value: int):
        if len(str(value)) < 7:
            raise ValueError("ID less than 7 chars")
        return value


class GetResourceRequests(BaseModel):
    project_tasks: List[GetResourceRequestsId]


class GetCompany(BaseModel):
    id_: int = Field(alias="id", strict=True)
    name: str
    owner_user_id: int
    employer_count_interval: int
    owner_post: str
    working_direction: str
    billing_tariff_id: int
    created_at: int
    updated_at: int
    logo: Optional[str] = None
    billing_is_over: bool
    companyOutboundWebhooks: list
    currency_id: int


class GetCompanies(BaseModel):
    companies: List[GetCompany]
