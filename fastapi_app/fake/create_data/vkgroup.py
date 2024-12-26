from datetime import datetime, timedelta
import factory
import factory.fuzzy
from sqlalchemy.orm import Session
from fastapi_app.ormmodel import VKGroup, Query, Position
from fastapi_app.data.init import engine


class GroupFactory(factory.Factory):
    class Meta:
        model = VKGroup

    name = factory.Sequence(lambda n: 'vkgroup%s' % n)


class QueryFactory(factory.Factory):
    class Meta:
        model = Query
    query = factory.Sequence(lambda n: 'query%s' % n)
    vkgroup_id = factory.SubFactory(GroupFactory)


class PositionFactory(factory.Factory):
    class Meta:
        model = Position
    position = factory.fuzzy.FuzzyChoice(range(-1, 100))
    created_at = datetime.now()
    query_id = factory.SubFactory(QueryFactory)


def get_time(n):
    now = datetime.now()
    return now - timedelta(days=n)


def create_data():
    with Session(engine) as session:
        fake_groups = [GroupFactory() for _ in range(10)]
        session.add_all(fake_groups)
        session.flush()

        for group in fake_groups:
            queries = [QueryFactory(vkgroup=group) for _ in range(5)]
            session.add_all(queries)
            session.flush()

            for query in queries:
                fake_times = [
                    get_time(n) for n in range(6, -1, -1)
                ]
                positions = [
                    PositionFactory(created_at=fake_time, query=query)
                    for fake_time in fake_times
                ]
                session.add_all(positions)
        session.commit()


if __name__ == "__main__":
    create_data()
