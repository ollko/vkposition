from sqlalchemy import Table, Column, Integer, String

from .base import Base

users = Table(
    'user', Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('hash', String),
)
