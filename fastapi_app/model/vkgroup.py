from pydantic import BaseModel, ConfigDict

from .query import Query


class VKGroup_(BaseModel):
    name: str


class VKGroup(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    vkgroup_id: int
    name: str


class VKGroupSchema(VKGroup):
    queries: list[Query]
