from sqlalchemy import select
from sqlalchemy.orm import joinedload, Session

from .init import engine
from fastapi_app.model.vkgroup import VKGroup_, VKGroup, VKGroupSchema
from fastapi_app.ormmodel.vkgroup import (
    VKGroup as OrmVKGroup,
    Query as OrmQuery,
    Position as OrmPosition,
)


def pymodel_to_ormmodel(group: VKGroup_) -> OrmVKGroup:
    return OrmVKGroup(name=group.name)


def get_one(vkgroup_id: int) -> VKGroup:
    with Session(engine) as session:
        stmt = (select(OrmVKGroup).where(OrmVKGroup.vkgroup_id == vkgroup_id)
                .options(joinedload(OrmVKGroup.queries))
                )
        group = session.scalars(stmt).unique().first()
        if group:
            return VKGroupSchema.model_validate(group)
        return None


def get_all() -> list[VKGroupSchema]:
    with Session(engine) as session:
        stmt = (select(OrmVKGroup)
                .join(OrmVKGroup.queries)

                )
        groups = session.scalars(stmt).unique().all()
        schema_group = [VKGroupSchema.model_validate(
            group) for group in groups]
    return schema_group


def create(group: VKGroup) -> VKGroup:
    orm_group = pymodel_to_ormmodel(group)
    with Session(engine) as session:
        session.add(orm_group)
        session.commit()
        return VKGroup.model_validate(orm_group)


# def delete(group: VKGroup) -> bool:
#     q = "delete from group where group_id = :group_id"
#     params = {"group_id": group.group_id}
#     res = curs.execute(q, params)
#     return bool(res)
