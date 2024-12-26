from sqlalchemy.orm import relationship
from sqlalchemy import (Column, Integer, String, Table,
                        ForeignKey, DateTime, func)

from .base import Base


class VKGroup(Base):
    __tablename__ = 'vkgroup'
    vkgroup_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    queries = relationship(
        "Query", back_populates='vkgroup')


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
