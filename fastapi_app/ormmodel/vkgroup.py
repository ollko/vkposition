from sqlalchemy.orm import relationship
from sqlalchemy import (Column, Integer, String, Table,
                        ForeignKey, DateTime, func)

from .base import Base


# Declare Classes / Tables
vkgroup_query = Table('vkgroup_query', Base.metadata,
                      Column('vkgroup_id', ForeignKey(
                          'vkgroup.vkgroup_id'), primary_key=True),
                      Column('query_id', ForeignKey(
                          'query.query_id'), primary_key=True)
                      )


class VKGroup(Base):
    __tablename__ = 'vkgroup'
    vkgroup_id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)
    queries = relationship(
        "Query", secondary=vkgroup_query, back_populates='vkgroups')


class Query(Base):
    __tablename__ = 'query'
    query_id = Column(Integer, primary_key=True)
    query = Column(String, nullable=False, unique=True)
    vkgroups = relationship("VKGroup", secondary=vkgroup_query,
                            back_populates='queries')


class Position(Base):
    __tablename__ = 'position'
    position_id = Column(Integer, primary_key=True)
    vkgroup_id = Column(ForeignKey('vkgroup.vkgroup_id'))
    query_id = Column(ForeignKey('query.query_id'))
    position = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, server_default=func.now())
