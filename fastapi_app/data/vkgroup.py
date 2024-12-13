from sqlalchemy import select
from sqlalchemy.orm import Session

from .init import engine
from fastapi_app.model.vkgroup import VKGroup_, VKGroup
from fastapi_app.ormmodel.vkgroup import VKGroup as OrmVKGroup


def ormmodel_to_pymodel(ormgroup: OrmVKGroup) -> VKGroup:
    return VKGroup(group_id=ormgroup.vkgroup_id,
                   name=ormgroup.name)


def pymodel_to_ormmodel(group: VKGroup_) -> OrmVKGroup:
    return OrmVKGroup(name=group.name)


def get_one(group_id: int | None = None,
            name: str | None = None) -> VKGroup:
    with Session(engine) as session:
        if group_id:
            stmt = select(OrmVKGroup).where(OrmVKGroup.vkgroup_id == group_id)
        elif name:
            stmt = select(OrmVKGroup).where(OrmVKGroup.name == name)
        group = session.scalars(stmt).first()
        if group:
            return ormmodel_to_pymodel(group)
    return None


def get_all() -> list[VKGroup]:
    with Session(engine) as session:
        stmt = select(OrmVKGroup)
        orm_groups = session.scalars(stmt).all()

    return [ormmodel_to_pymodel(orm_group) for orm_group in orm_groups]


def create(group: VKGroup) -> VKGroup:
    orm_group = pymodel_to_ormmodel(group)
    with Session(engine) as session:
        session.add(orm_group)
        session.commit()
    return get_one(name=group.name)


# def modify(vkgroup: VKGroup) -> VKGroup:
#     q = """update group
#             set group_id=:group_id,
#             name=:name,
#             active=:active,
#             where group_id=:group_id_orig"""
#     params = model_to_dict(vkgroup)
#     params["group_id_orig"] = vkgroup.group_id
#     _ = curs.execute(q, params)
#     return get_one(vkgroup.group_id)


# def delete(group: VKGroup) -> bool:
#     q = "delete from group where group_id = :group_id"
#     params = {"group_id": group.group_id}
#     res = curs.execute(q, params)
#     return bool(res)
