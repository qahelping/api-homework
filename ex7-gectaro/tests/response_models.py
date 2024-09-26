from typing import Optional

from pydantic import BaseModel, Field


class ResourceRequest(BaseModel):
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


class ResourceRequestResponse(BaseModel):
    project_tasks: list[ResourceRequest]


class CreateResourceRequestBody(BaseModel):
    project_tasks_resource_id: int
    volume: float
    cost: float
    needed_at: int


data = [
    {
        "id": 9395666,
        "project_tasks_resource_id": 12738591,
        "volume": "135.0000000000",
        "cost": "6254.0000000000",
        "batch_number": None,
        "batch_parent_request_id": None,
        "is_over_budget": False,
        "created_at": 1719383226,
        "updated_at": 1719383226,
        "user_id": 23019,
        "needed_at": 1729978012,
        "created_by": 23019
    },
    {
        "id": 9395665,
        "project_tasks_resource_id": 12738590,
        "volume": "8.8100000000",
        "cost": "2400.0000000000",
        "batch_number": None,
        "batch_parent_request_id": None,
        "is_over_budget": False,
        "created_at": 1719383226,
        "updated_at": 1719383226,
        "user_id": 23019,
        "needed_at": 1729978012,
        "created_by": 23019
    }
]
