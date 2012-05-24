# -*- coding: utf-8 -*-

from odd.data.db import Model

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP, TEXT

class Tag_Follow(Model):
    __tablename__ = 'tag_follows'
    
    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT, ForeignKey('users.id'), nullable=False)
    tag = Column('tag', VARCHAR(50), nullable=False)

    def __init__(self, user_id, tag):
        self.user_id = user_id
        self.tag = tag

    def __repr__(self):
        return '<Tag_Follow %d %d>' % (self.user_id, self.tag)
