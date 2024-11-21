

from fastapi_app.model.vkgroup import VKGroup
import fastapi_app.data.vkgroup as data


def get_all() -> list[VKGroup]:
    return data.get_all()


def get_one(vkgroup_id: int) -> VKGroup | None:
    return data.get(vkgroup_id)


def create(creature: VKGroup) -> VKGroup:
    return data.create(creature)


def replace(group_id: int, group: VKGroup) -> VKGroup:
    return data.replace(vkgroup_id, vkgroup)


def delete(group_id) -> bool:
    return data.delete(vkgroup_id)
