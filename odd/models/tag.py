# -*- coding: utf-8 -*-

from odd.data.db import Model

from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, VARCHAR

class Question_Tag(Model):
    __tablename__ = 'question_tags'
    
    id = Column('id', INT, primary_key=True)
    question_id = Column('question_id', INT, ForeignKey('questions.id'), nullable=False)
    tag = Column('tag', VARCHAR(50), nullable=False)

    def __init__(self, question_id, tag):
        self.question_id = question_id
        self.tag = tag

    def __repr__(self):
        return '<Question_Tag %d %s>' % (self.question_id,self.tag)
