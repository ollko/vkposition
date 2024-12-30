from pydantic import BaseModel, ConfigDict
from .vkgroup import Position


class GroupsTableRow(BaseModel):
    group_id: int
    group: str
    mumber: int
    avg_position: int
    dynamic: str
    top: str
    group_url: str
