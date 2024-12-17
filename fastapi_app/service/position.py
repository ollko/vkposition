from fastapi_app.data import position as data
from fastapi_app.model.position import Position_, Position


def create_position(position: Position_) -> Position_:
    return data.create_position(position)


def get_vkgroup_positions(group_id: int) -> list[Position] | None:
    return data.get_group_positions(group_id)
