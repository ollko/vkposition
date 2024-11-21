from pydantic import BaseModel


class VKGroup(BaseModel):
    group_id: int
    name: str
    active: bool
