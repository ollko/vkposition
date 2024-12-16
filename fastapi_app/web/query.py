from fastapi import APIRouter

from fastapi_app.model.vkgroup import Query_, Query, QuerySchema
from fastapi_app.service import query as service

router = APIRouter(prefix="/query")


@router.get("/")
def query_list() -> list[QuerySchema]:
    return service.get_all()


@router.get("/{query_id}/")
def get_query(query_id) -> QuerySchema:
    return service.get_one(query_id)


@router.post("/")
def create_query(query: Query_) -> Query:
    return service.create(query)


@router.patch("/")
def modify(query: Query) -> Query:
    return service.modify(query)


@router.delete("/{query_id}")
def del_group(query_id: int):
    return service.delete(query_id)
