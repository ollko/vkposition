from fastapi_app.model.user import User
from .init import (conn, curs, get_db, IntegrityError)
from fastapi_app.error import Missing, Duplicate


curs.execute("""create table if not exists
                user(
                name text primary key,
                hash text)""")

curs.execute("""create table if not exists
                xuser(
                name text primary key,
                hash text)""")


def row_to_model(row: tuple) -> User:
    name, hash = row
    return User(name=name, hash=hash)


def model_to_dict(user: User) -> dict:
    return user.dict()


def get_one(name: str) -> User:
    print(f'{name=}')
    qry = "select * from user where name=:name"
    params = {"name": name}
    curs.execute(qry, params)
    row = curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"User {name} not found")


def get_all() -> list[User]:
    qry = "select * from user"
    curs.execute(qry)
    return [row_to_model(row) for row in curs.fetchall()]


def create(user: User, table: str = "user"):
    """Добавление <пользователя> в таблицу user или xuser"""
    qry = f"""insert into {table}
            values
            (:name, :hash)"""
    params = model_to_dict(user)
    try:
        curs.execute(qry, params)
    except IntegrityError:
        raise Duplicate(msg=f"{table}: user {user.name} already exists")
    except Exception as e:
        print(e)


def modify(name: str, user: User) -> User:
    qry = """update user set
            name=:name, hash=:hash
            where name=:name0"""
    params = {
        "name": user.name,
        "hash": user.hash,
        "name0": name}
    curs.execute(qry, params)
    if curs.rowcount == 1:
        return get_one(user.name)
    else:
        raise Missing(msg=f"User {name} not found")


def delete(name: str) -> None:
    """Удаление пользователя с именем <name> из таблицы пользователей,
    добавление его в таблицу xuser"""
    user = get_one(name)
    qry = "delete from user where name = :name"
    params = {"name": name}
    curs.execute(qry, params)
    if curs.rowcount != 1:
        raise Missing(msg=f"User {name} not found")
    create(user, table="xuser")
