from fastapi import APIRouter
from fastapi_app.model.group_position import PositionRow
from fastapi_app.service import group_position as service

router = APIRouter(prefix="/position")


@router.get("/")
def position_table() -> list[PositionRow]:
    return service.get_all()


@router.get("/{group_id}")
def position_table() -> list[PositionRow]:
    return service.get_all()
