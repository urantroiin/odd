# -*- coding: utf-8 -*-

from os import listdir
from os.path import join
from datetime import datetime

from sqlalchemy.orm import relation, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP, TEXT

from odd import app
from odd.data.db import Model

class Resource(Model):
    __tablename__ = 'resources'
    
    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT, ForeignKey('users.id'), nullable=False)
    title = Column('title', VARCHAR(50), nullable=False)
    desc = Column('description', TEXT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)
    download_count = Column('download_count', INT, nullable=False)
    
    user = relation('User')
    tags = relation("Resource_Tag", backref=backref('resource'))

    def __init__(self, user_id, title, desc, tags):
        self.user_id = user_id
        self.title = title
        self.desc = desc
        self.tags = [Resource_Tag(self.id, tag) for tag in tags]
        self.create_time = datetime.now()
        self.download_count = 0

    def file_list(self):
        path = join(app.static_folder, 'resources', str(self.id))
        return listdir(path)
        
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

class Resource_Download(Model):
    __tablename__ = 'resource_downloads'
    
    id = Column('id', INT, primary_key=True)
    resource_id = Column('resource_id', INT, nullable=False)
    user_id = Column('user_id', INT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    def __init__(self, resource_id, user_id):
        self.resource_id = resource_id
        self.user_id = user_id
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Resource_Download %d %s>' % (self.resource_id,self.user_id)
