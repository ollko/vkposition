from .init import curs
from fastapi_app.model.vkgroup import VKGroup

curs.execute(
    """create table if not exists vkgroup (group_id integer primary key,
        name text, active bool);""")


def row_to_model(row: tuple) -> VKGroup:
    (group_id, name, active) = row
    return VKGroup(group_id, name, active)


def model_to_dict(group: VKGroup) -> dict:
    return group.dict()


def get_one(group_id: str) -> VKGroup:
    q = "select * from vkgroup where group_id=:group_id"
    params = {"group_id": group_id}
    curs.execute(q, params)
    return row_to_model(curs.fetchone())


def get_all() -> list[VKGroup]:
    q = "select * from vkgroup"
    curs.execute(q)
    return [row_to_model(row) for row in curs.fetchall()]


def create(group: VKGroup) -> VKGroup:
    q = "insert into vkgroup values"
    "(:group_id, :name, :active)"
    params = model_to_dict(group)
    curs.execute(q, params)
    return get_one(group.group_id)


def modify(vkgroup: VKGroup) -> VKGroup:
    q = """update group
            set group_id=:group_id,
            name=:name,
            active=:active,
            where group_id=:group_id_orig"""
    params = model_to_dict(vkgroup)
    params["group_id_orig"] = vkgroup.group_id
    _ = curs.execute(q, params)
    return get_one(vkgroup.group_id)


def delete(group: VKGroup) -> bool:
    q = "delete from group where group_id = :group_id"
    params = {"group_id": group.group_id}
    res = curs.execute(q, params)
    return bool(res)
