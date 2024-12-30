from datetime import datetime
from pydantic import BaseModel, ConfigDict


class Position_(BaseModel):
    position: int
    created_at: datetime


class Position(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    position_id: int
    position: int
    created_at: datetime


class Query_(BaseModel):
    query: str


class Query(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    query_id: int
    query: str


class QuerySchema(Query):
    positions: list[Position]


class VKGroup_(BaseModel):
    name: str


class VKGroup(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    vkgroup_id: int
    name: str
    avg_position: int


class VKGroupSchema(VKGroup):
    queries: list[QuerySchema]
