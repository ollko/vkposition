from fastapi import APIRouter
from fastapi_app.model.position import Position_, Position
from fastapi_app.service import position as service

router = APIRouter(prefix="/position")


@router.post("/")
def create_position(position: Position_) -> Position:
    return service.create_position(position)


@router.get("/{vkgroup_id}")
def vkgroup_position(vkgroup_id: int) -> list[Position] | None:
    return service.get_vkgroup_positions(vkgroup_id)
