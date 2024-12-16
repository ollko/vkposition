from fastapi_app.model.vkgroup import Query_, Query
import fastapi_app.data.query as data


def get_all(active: bool | None = None) -> list[Query]:
    return data.get_all()


def get_one(query_id: int) -> Query | None:
    return data.get_one(query_id)


def create(query: Query_) -> Query:
    return data.create(query)


def replace(query_id: int, query: Query) -> Query:
    return data.replace(query_id, query)


def delete(query_id) -> bool:
    return data.delete(query_id)
