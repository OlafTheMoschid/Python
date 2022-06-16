from datetime import datetime

import sqlalchemy
from sqlalchemy import PickleType
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Video(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'videos'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    link = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    author = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    comments = sqlalchemy.Column(MutableList.as_mutable(PickleType),
                                 default=[], nullable=True)
    upload_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                    default=datetime.now)
