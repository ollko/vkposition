from sqlalchemy import select
from sqlalchemy.orm import joinedload, Session

from .init import engine
from fastapi_app.model.vkgroup import Query_, Query, QuerySchema
from fastapi_app.ormmodel.vkgroup import Query as OrmQuery


def pymodel_to_ormmodel(query: Query_) -> OrmQuery:
    return OrmQuery(name=query.query)


def get_one(query_id: int) -> Query:
    with Session(engine) as session:
        stmt = (select(OrmQuery, query_id)
                .options(joinedload(OrmQuery.vkgroups))
                )
        query = session.scalars(stmt).unique().first()
        if query:
            return QuerySchema.model_validate(query)
        return None


def get_all() -> list[QuerySchema]:
    with Session(engine) as session:
        stmt = select(OrmQuery).options(joinedload(OrmQuery.vkgroups))
        queries = session.scalars(stmt).unique().all()
        schema_query = [QuerySchema.model_validate(query) for query in queries]
    return schema_query


def create(query: Query) -> Query:
    orm_query = pymodel_to_ormmodel(query)
    with Session(engine) as session:
        session.add(orm_query)
        session.commit()
        return Query.model_validate(orm_query)
