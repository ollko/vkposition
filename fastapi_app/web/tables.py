from fastapi import APIRouter, Request

from fastapi_app.model.vkgroup import VKGroupSchema
from fastapi_app.service import tables as service
router = APIRouter(prefix="/group-table")


@router.get("/")
def vkgroup_list(request: Request) -> list[VKGroupSchema]:
    from fastapi_app.main import templates
    data = service.groups_table_data()
    return templates.TemplateResponse("group_positions.html",
                                      {"request": request, "data": data})
