from pydantic import BaseModel, ConfigDict


class Query_(BaseModel):
    phrase: str


class Query(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    query_id: int
    phrase: str
