
from fastapi import APIRouter

from fastapi_app.model.vkgroup import VKGroup
# from fastapi_app.fake import group as service
from fastapi_app.service import vkgroup as service

router = APIRouter(prefix="/group")


@router.get("/")
def vkgroup_list(active: bool | None = None):
    if active is not None:
        return service.get_all(active)
    else:
        return service.get_all()


@router.get("/{vkgroup_id}/")
def get_group(vkgroup_id: int):
    return service.get_one(vkgroup_id)


@router.post("/")
def create_group(vkgroup: VKGroup) -> VKGroup:
    return service.create(vkgroup)


@router.patch("/")
def modify(vkgroup: VKGroup) -> VKGroup:
    return service.modify(vkgroup)


@router.delete("/{vkgroup_id}")
def del_group(vkgroup_id: int):
    return service.delete(vkgroup_id)
