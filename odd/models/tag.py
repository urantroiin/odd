# -*- coding: utf-8 -*-

from datetime import datetime
from os.path import isfile, join

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, VARCHAR, TEXT, TIMESTAMP

from odd import app
from odd.data.db import Model

class Tag(Model):
    __tablename__ = 'tags'
    
    id = Column('id', INT, primary_key=True)
    tag = Column('tag', VARCHAR(50), nullable=False)
    description = Column('description', TEXT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    def __init__(self, tag, description=''):
        self.tag = tag
        self.description = description
        self.create_time = datetime.now()

    def tag_photo(self,size):
        name = 'tag_photo/%d-%d.jpg'
        filename = name % (self.id, size)
        if isfile(join(app.static_folder, filename)):
            return filename
        
        filename = name % (0, size)
        if isfile(join(app.static_folder, filename)):
            return filename

        filename = name % (0, 20)
        if isfile(join(app.static_folder, filename)):
            return filename

    def __repr__(self):
        return '<Tag %s>' % self.tag

class Tag_Edit(Model):
    __tablename__ = 'tag_edits'
    
    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT, nullable=False)
    tag_id = Column('tag_id', INT, nullable=False)
    description = Column('description', TEXT, nullable=False)
    photo = Column('photo', INT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    def __init__(self, user_id, tag_id, description, photo):
        self.user_id = user_id
        self.tag_id = tag_id
        self.description = description
        self.photo = photo
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Tag_Edit %s>' % self.id
