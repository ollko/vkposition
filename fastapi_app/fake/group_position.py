from fastapi_app.model.group_position import PositionRow


_positions = [
    PositionRow(
        key=1,
        group='ёжики',
        group_count=100,
        avg_position=2,
        dynamic='+0 =6 -0',
        top='0 13 0',
        group_url='127.0.0.1:8008/group/1'
    ),
    PositionRow(
        key='2',
        group='зайцы',
        group_count=100,
        avg_position=2,
        dynamic='+0 =6 -0',
        top='0 13 0',
        group_url='127.0.0.1:8008/group/2'
    ),
    PositionRow(
        key='3',
        group='овцы',
        group_count=100,
        avg_position=2,
        dynamic='+0 =6 -0',
        top='0 13 0',
        group_url='127.0.0.1:8008/group/3'
    ),
    PositionRow(
        key='4',
        group='перепелки',
        group_count=100,
        avg_position=2,
        dynamic='+0 =6 -0',
        top='0 13 0',
        group_url='127.0.0.1:8008/group/4'
    )
]


def get_all() -> list[PositionRow]:
    return _positions
