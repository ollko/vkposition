import os
from fastapi_app.model.group_position import PositionRow
if os.getenv('VKGROUP_UNIT_TEST'):
    from fastapi_app.fake.group_position import _positions


def get_all() -> list[PositionRow]:
    return [PositionRow(position) for position in _positions]
