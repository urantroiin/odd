# -*- coding: utf-8 -*-

from odd.data.db import Model

from sqlalchemy.schema import Column
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP, TEXT

from datetime import datetime

class Tag(Model):
    __tablename__ = 'tags'
    
    id = Column('id', INT, primary_key=True)
    name = Column('name', VARCHAR(32), unique=True, nullable=False)
    desc = Column('description', TEXT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    def __init__(self, name, desc=''):
        self.name = name
        self.desc = desc
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Tag %r>' % self.name

class Tag_User(Model):
    __tablename__ = 'tag_users'
    
    id = Column('id', INT, primary_key=True)
    tag_id = Column('tag_id', INT, nullable=False)
    user_id = Column('user_id', INT, nullable=False)

    def __init__(self, tag_id, user_id):
        self.tag_id = tag_id
        self.user_id = user_id

    def __repr__(self):
        return '<Tag_User %d %d>' % (self.tag_id,self.user_id)
