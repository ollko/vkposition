from sqlalchemy.orm import relationship, object_session
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy import (Column, Integer, String,
                        ForeignKey, DateTime, func, text, )

from .base import Base


class VKGroup(Base):
    __tablename__ = 'vkgroup'
    vkgroup_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    members = Column(Integer, nullable=True, default=0)
    queries = relationship(
        "Query", back_populates='vkgroup')

    @hybrid_property
    def avg_position(self):
        stmt = '''
            SELECT avg(position.position_id)
            FROM position
            JOIN query ON position.query_id=query.query_id
            WHERE query.vkgroup_id =:vkgroupid
            '''
        result = object_session(self)\
            .scalars(text(stmt), params={'vkgroupid': self.vkgroup_id}).one()
        return result


league = relationship("League",
                      secondary="teams",
                      primaryjoin="Game.home_team_id == Team.id",
                      secondaryjoin="Team.league_id == League.id",
                      viewonly=True)


class Query(Base):
    __tablename__ = 'query'
    query_id = Column(Integer, primary_key=True)
    query = Column(String, nullable=False, unique=True)
    vkgroup_id = Column(ForeignKey('vkgroup.vkgroup_id', ondelete='CASCADE'))
    vkgroup = relationship(
        VKGroup, back_populates='queries'
    )
    positions = relationship(
        'Position', back_populates='query'
    )


class Position(Base):
    __tablename__ = 'position'
    position_id = Column(Integer, primary_key=True)
    position = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
    query_id = Column(ForeignKey('query.query_id', ondelete='CASCADE'))
    query = relationship(
        Query, back_populates='positions'
    )
