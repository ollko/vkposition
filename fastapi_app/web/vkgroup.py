
from fastapi import APIRouter

from fastapi_app.model.vkgroup import VKGroup_, VKGroup, VKGroupSchema
from fastapi_app.service import vkgroup as service

router = APIRouter(prefix="/group")


@router.get("/")
def vkgroup_list() -> list[VKGroupSchema]:
    return service.get_all()


@router.get("/{vkgroup_id}/")
def get_group_id(vkgroup_id):
    return service.get_one(vkgroup_id)


@router.post("/")
def create_group(vkgroup: VKGroup_) -> VKGroup:
    return service.create(vkgroup)


@router.patch("/")
def modify(vkgroup: VKGroup) -> VKGroup:
    return service.modify(vkgroup)


@router.delete("/{vkgroup_id}")
def del_group(vkgroup_id: int):
    return service.delete(vkgroup_id)
