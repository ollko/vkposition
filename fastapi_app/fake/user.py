from fastapi_app.model.user import User
from fastapi_app.error import Missing, Duplicate

# (в этом модуле нет проверки хешированного пароля)
fakes = [
    User(name="kwijobo",
         hash="abc"),
    User(name="ermagerd",
         hash="xyz"),
]


def find(name: str) -> User | None:
    for e in fakes:
        if e.name == name:
            return e
    return None


def check_missing(name: str):
    if not find(name):
        raise Missing(msg=f"Missing user {name}")


def check_duplicate(name: str):
    if find(name):
        raise Duplicate(msg=f"Duplicate user {name}")


def get_all() -> list[User]:
    """Возврат всех пользователей"""
    return fakes


def get_one(name: str) -> User:
    """Возврат одного пользователя"""
    check_missing(name)
    return find(name)


def modify(name: str, user: User) -> User:
    """Частичное изменение пользователя"""
    check_missing(name)
    return user


def delete(name: str) -> None:
    """Удаление пользователя"""
    check_missing(name)
    return None