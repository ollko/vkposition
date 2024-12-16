from pydantic import BaseModel, ConfigDict


class VKGroup_(BaseModel):
    name: str


class VKGroup(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    vkgroup_id: int
    name: str


class VKGroupSchema(VKGroup):
    queries: list['Query']


class Query_(BaseModel):
    phrase: str


class Query(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    query_id: int
    phrase: str


class QuerySchema(Query):
    vkgroups: list[VKGroup]
