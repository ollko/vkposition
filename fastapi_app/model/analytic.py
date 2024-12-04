from pydantic import BaseModel


class VKGroup(BaseModel):
    name: str
    members_count: int
    avg_position: int
    dynamic: int


class Query(BaseModel):
    query: str
