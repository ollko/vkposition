from fastapi_app.model.group_position import (
    Position,
    PositionRow,
    PositionTable,
    GroupTable,
)

_positions = GroupTable(
    title='Проверка позиций групп ВК',
    main_page_url='position',
    query_delete_url='query/del',
    query_add_url='query/add',
    columns=['запрос', '01.12.2024', '02.12.2024', '03.12.2024',
             '04.12.2024', '05.12.2024', '06.12.2024', '07.12.2024']
    rows=[
        Position(
            position=5,
            at_time='01.12.2024',
        ),
        Position(
            position=3,
            at_time='02.12.2024',
        ),
        Position(
            position=0,
            at_time='03.12.2024',
        ),
        Position(
            position=-3,
            at_time='04.12.2024',
        ),
        Position(
            position=0,
            at_time='05.12.2024',
        ),
        Position(
            position=-7,
            at_time='06.12.2024',
        ),
        Position(
            position=4,
            at_time='07.12.2024',
        ),
    ]
)
