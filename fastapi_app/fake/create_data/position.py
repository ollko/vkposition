from datetime import datetime, timedelta
import random

from sqlalchemy.orm import Session

from fastapi_app.ormmodel.vkgroup import Position
from fastapi_app.data import query as data
from fastapi_app.data.init import engine

now = datetime.now()


def get_time(n):
    return now - timedelta(days=n)


fake_time = [
    get_time(n) for n in range(6, -1, -1)
]


def get_fake_position():
    return random.randrange(-1, 50)


def create():
    with Session(engine) as session:
        queries_with_groups = data.get_all()
        for t in fake_time:
            for query in queries_with_groups:
                positions = [Position(vkgroup_id=vkgroup.vkgroup_id,
                                      query_id=query.query_id,
                                      position=get_fake_position(),
                                      created_at=t)
                             for vkgroup in query.vkgroups]
                session.add_all(positions)
                session.flush()
        session.commit()


create()
