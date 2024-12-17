import os
from fastapi_app.model.position import PositionRow

if os.getenv('VKGROUP_UNIT_TEST'):
    import fastapi_app.fake.group_position as data
else:
    import fastapi_app.data.group_position as data


def get_all() -> list[PositionRow]:
    return data.get_all()
