# -*- coding: utf-8 -*-

from odd.data.db import Model

from sqlalchemy.schema import Column
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP, TEXT

from datetime import datetime

class Group(Model):
    __tablename__ = 'groups'
    
    id = Column('id', INT, primary_key=True)
    name = Column('name', VARCHAR(32), unique=True, nullable=False)
    desc = Column('description', TEXT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    def __init__(self, name, desc=''):
        self.name = name
        self.desc = desc
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Group %r>' % self.name

class Group_User(Model):
    __tablename__ = 'group_users'
    
    id = Column('id', INT, primary_key=True)
    group_id = Column('group_id', INT, nullable=False)
    user_id = Column('user_id', INT, nullable=False)

    def __init__(self, group_id, user_id):
        self.group_id = group_id
        self.user_id = user_id

    def __repr__(self):
        return '<Group_User %d %d>' % (self.group_id,self.user_id)
