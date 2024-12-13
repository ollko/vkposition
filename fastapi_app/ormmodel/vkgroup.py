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
    name = Column(String, nullable=False)
    queries = relationship(
        "Query", secondary=vkgroup_query, back_populates='vkgroups')


class Query(Base):
    __tablename__ = 'query'
    query_id = Column(Integer, primary_key=True)
    phrase = Column(String, nullable=False)
    vkgroups = relationship("VKGroup", secondary=vkgroup_query,
                            back_populates='queries')


parse_event = Table('parse_ivent', Base.metadata,
                    Column('parse_ivent_id', Integer, primary_key=True),
                    Column('vkgroup_id', ForeignKey(
                        'vkgroup.vkgroup_id')),
                    Column('query_id', ForeignKey(
                        'query.query_id')),
                    Column('position', Integer, nullable=False),
                    Column('at_time', DateTime(timezone=True),
                           nullable=False,
                           server_default=func.now())
                    )
