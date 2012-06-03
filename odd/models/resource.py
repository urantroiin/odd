# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy.orm import relation, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP, TEXT

from odd.data.db import Model

class Resource(Model):
    __tablename__ = 'resources'
    
    id = Column('id', INT, primary_key=True)
    title = Column('title', VARCHAR(50), nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)
    
    tags = relation("Resource_Tag", backref=backref('resource'))

    def __init__(self, title):
        self.title = title
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Resource %r>' % self.title

class Resource_Tag(Model):
    __tablename__ = 'resource_tags'
    
    id = Column('id', INT, primary_key=True)
    resource_id = Column('resource_id', INT, ForeignKey('resources.id'), nullable=False)
    tag = Column('tag', VARCHAR(50), nullable=False)

    def __init__(self, resource_id, tag):
        self.resource_id = resource_id
        self.tag = tag

    def __repr__(self):
        return '<Resource_Tag %d %s>' % (self.resource_id,self.tag)
