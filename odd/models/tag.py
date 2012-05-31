# -*- coding: utf-8 -*-


from datetime import datetime

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP

from odd.data.db import Model

class Tag(Model):
    __tablename__ = 'tags'
    
    id = Column('id', INT, primary_key=True)
    tag = Column('tag', VARCHAR(50), nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    def __init__(self, tag):
        self.tag = tag
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Tag %s>' % self.tag
