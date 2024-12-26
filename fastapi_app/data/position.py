from sqlalchemy import select
from sqlalchemy.orm import joinedload, Session

from .init import engine
from fastapi_app.model.vkgroup import Position_, Position
from fastapi_app.ormmodel.vkgroup import Position as OrmPosition


def pydantic_to_orm_model(position: Position_) -> OrmPosition:
    dump = position.model_dump()
    return OrmPosition(**dump)


def create_position(position: Position_) -> Position:
    orm_position = pydantic_to_orm_model(position)
    with Session(engine) as session:
        session.add(orm_position)
        session.commit()
        return Position.model_validate(orm_position)


def get_group_positions(vkgroup_id: int) -> list[Position] | None:
    with Session(engine) as session:
        stmt = select(OrmPosition).where(OrmPosition.vkgroup_id == vkgroup_id)
        positions = session.scalars(stmt).all()
        if positions:
            return [Position.model_validate(position) for position in positions]
        return None
