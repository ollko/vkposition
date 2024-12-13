

from fastapi_app.model.vkgroup import VKGroup_, VKGroup
import fastapi_app.data.vkgroup as data


def get_all(active: bool | None = None) -> list[VKGroup]:
    return data.get_all()


def get_one(vkgroup_id: int | None = None,
            name: str | None = None) -> VKGroup | None:
    if vkgroup_id:
        return data.get_one(group_id=vkgroup_id)
    elif name:
        return data.get_one(name=name)


def create(vkgroup: VKGroup_) -> VKGroup:
    return data.create(vkgroup)


def replace(vkgroup_id: int, vkgroup: VKGroup) -> VKGroup:
    return data.replace(vkgroup_id, vkgroup)


def delete(vkgroup_id) -> bool:
    return data.delete(vkgroup_id)
