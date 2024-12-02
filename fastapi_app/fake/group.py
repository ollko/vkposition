from ..model.vkgroup import Group

_groups = [
    Group(
        group_id=1,
        name='хищники',
        active=True
    ),
    Group(
        group_id=2,
        name='Боты',
        active=False)
]


def get_all(active: bool | None = None) -> list[Group]:
    if active is not None:
        groups = []
        for group in _groups:
            if group.active == active:
                groups.append(group)
        return groups
    else:
        return _groups


def get_one(group_id: int) -> Group | None:
    for group in _groups:
        if group.group_id == id:
            return group


def create(group: Group) -> Group:
    """Добавление группы"""
    return group


def modify(group: Group) -> Group:
    """Частичное изменение записи группы"""
    return group


def replace(group: Group) -> Group:
    """Полная замена записи группы"""
    return group


def delete(group_id: str) -> bool:
    """Удаление записи исследователя; возврат значения None,
    если запись существовала"""
    return None
