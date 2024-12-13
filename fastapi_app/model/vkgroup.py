from pydantic import BaseModel


class VKGroup_(BaseModel):
    name: str


class VKGroup(VKGroup_):
    group_id: int
