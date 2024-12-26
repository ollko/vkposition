from fastapi import APIRouter, Request

from fastapi_app.model.vkgroup import VKGroup_, VKGroup, VKGroupSchema
from fastapi_app.service import vkgroup as service
router = APIRouter(prefix="/group-table")


@router.get("/")
def vkgroup_list(request: Request) -> list[VKGroupSchema]:
    from fastapi_app.main import templates
    data = service.get_all()
    return templates.TemplateResponse("group_positions.html",
                                      {"request": request, "data": data})
