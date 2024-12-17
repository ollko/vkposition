from datetime import datetime
from pydantic import BaseModel, ConfigDict


class Position_(BaseModel):
    vkgroup_id: int
    query_id: int
    position: int


class Position(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    position_id: int
    vkgroup_id: int
    query_id: int
    position: int
    created_at: datetime


# class Position(BaseModel):
#     key: int
#     group: str
#     group_count: int
#     avg_position: int
#     dynamic: str
#     top: str
#     group_url: str
