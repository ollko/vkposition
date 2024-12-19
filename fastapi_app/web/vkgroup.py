
from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from fastapi_app.model.vkgroup import VKGroup_, VKGroup, VKGroupSchema
from fastapi_app.service import vkgroup as service

router = APIRouter(prefix="/group")


@router.get("/")
def vkgroup_list() -> list[VKGroupSchema]:
    return service.get_all()


@router.get("/{vkgroup_id}/")
def get_group_id(vkgroup_id) -> VKGroupSchema:
    return service.get_one(vkgroup_id)


@router.post("/")
def create_group(
        name: str = Form(...)):
    vkgroup = VKGroup_(name=name)
    service.create(vkgroup)
    return RedirectResponse(url="/query/", status_code=303)


@router.patch("/")
def modify(vkgroup: VKGroup) -> VKGroup:
    return service.modify(vkgroup)


@router.delete("/{vkgroup_id}/")
def del_group(vkgroup_id: int):
    return service.delete(vkgroup_id)
