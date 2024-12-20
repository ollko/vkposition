import random
import factory
from sqlalchemy.orm import Session
from fastapi_app.ormmodel import VKGroup, Query
from fastapi_app.data.init import engine


class GroupFactory(factory.Factory):
    class Meta:
        model = VKGroup

    name = factory.Sequence(lambda n: 'group%s' % n)


class QueryFactory(factory.Factory):
    class Meta:
        model = Query

    query = factory.Sequence(lambda n: 'query%s' % n)


def create():
    with Session(engine) as session:

        fake_queries = [QueryFactory() for _ in range(20)]
        fake_group = [GroupFactory() for _ in range(10)]

        for group in fake_group:
            sample = random.sample(range(20), 5)
            group.queries = [
                fake_queries[i] for i in range(len(fake_queries))
                if i in sample
            ]
            group = GroupFactory()

        session.add_all(fake_queries + fake_group)
        session.commit()


if __name__ == "__main__":
    create()
