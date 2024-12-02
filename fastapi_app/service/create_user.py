from .user import get_hash
from fastapi_app.data import user as data
from fastapi_app.model.user import User


def create_new_user(name: str, password: str):
    user = User(name=name, hash=get_hash(password))
    return data.create(user)
