from fastapi_app.model.tables import GroupsTableRow
import fastapi_app.data.vkgroup as data


def groups_table_data(active: bool | None = None) -> list[GroupsTableRow]:
    groups = data.get_all()
    
    for group in groups:
        group_positions = []

        for query in group.queries:
            group_positions.extend([
                position.position for position in query.positions
            ])
        group.avg_position = sum(group_positions)/len(group_positions)
