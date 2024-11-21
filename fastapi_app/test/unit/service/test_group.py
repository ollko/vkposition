from fastapi_app.model.vkgroup import Group
from fastapi_app.service import group as code


sample = Group(group_id=1,
               name='Бот',
               active=False)


def test_create():
    resp = code.create(sample)
    assert resp == sample


def test_get_exists():
    resp = code.get_one(1)
    assert resp == sample


def test_get_missing():
    resp = code.get_one(5)
    assert resp is None
