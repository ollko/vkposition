from pydantic import BaseModel, AnyUrl


class PositionRow(BaseModel):
    key: int
    group: str
    group_count: int
    avg_position: int
    dynamic: str
    top: str
    group_url: str
