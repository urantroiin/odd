# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy.orm import relation, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP, TEXT

from odd.data.db import Model

class Notice(Model):
    __tablename__ = 'notices'
    
    id = Column('id', INT, primary_key=True)
    title = Column('title', VARCHAR(255), nullable=False)
    content = Column('content', TEXT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)
    
    tags = relation("Notice_Tag", backref=backref('notice'))

    def __init__(self, title, content):
        self.title = title
        self.content = content
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Notice %r>' % self.title

class Notice_Tag(Model):
    __tablename__ = 'notice_tags'
    
    id = Column('id', INT, primary_key=True)
    notice_id = Column('notice_id', INT, ForeignKey('notices.id'), nullable=False)
    tag = Column('tag', VARCHAR(50), nullable=False)

    def __init__(self, notice_id, tag):
        self.notice_id = notice_id
        self.tag = tag

    def __repr__(self):
        return '<Notice_Tag %d %s>' % (self.notice_id,self.tag)
