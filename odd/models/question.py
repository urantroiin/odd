# -*- coding: utf-8 -*-

from odd.data.db import Model

from sqlalchemy.schema import Column
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP, TEXT

from datetime import datetime

class Question(Model):
    __tablename__ = 'questions'
    
    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT, nullable=False)
    title = Column('title', VARCHAR(255), nullable=False)
    content = Column('content', TEXT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    def __init__(self, user_id, title, content):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Question %r>' % self.title

class Question_Tag(Model):
    __tablename__ = 'question_tags'
    
    id = Column('id', INT, primary_key=True)
    question_id = Column('question_id', INT, nullable=False)
    tag = Column('tag', VARCHAR(50), nullable=False)

    def __init__(self, question_id, tag):
        self.question_id = question_id
        self.tag = tag

    def __repr__(self):
        return '<Question_Tag %d %s>' % (self.question_id,self.tag)
