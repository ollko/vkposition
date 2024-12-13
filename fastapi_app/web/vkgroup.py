
from fastapi import APIRouter

from fastapi_app.model.vkgroup import VKGroup_, VKGroup
# from fastapi_app.fake import group as service
from fastapi_app.service import vkgroup as service

router = APIRouter(prefix="/group")


@router.get("/")
def vkgroup_list(active: bool | None = None) -> list[VKGroup]:
    if active is not None:
        return service.get_all(active)
    else:
        return service.get_all()


@router.get("/{item_field}/")
def get_group_id(item_field):
    print('In get_group_id')
    try:
        item_field = int(item_field)
    except ValueError:
        return service.get_one(name=item_field)
    else:
        return service.get_one(vkgroup_id=item_field)


@router.post("/")
def create_group(vkgroup: VKGroup_) -> VKGroup:
    return service.create(vkgroup)


@router.patch("/")
def modify(vkgroup: VKGroup) -> VKGroup:
    return service.modify(vkgroup)


@router.delete("/{vkgroup_id}")
def del_group(vkgroup_id: int):
    return service.delete(vkgroup_id)
