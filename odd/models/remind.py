# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy.orm import relation, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, Boolean, TIMESTAMP, VARCHAR

from odd.data.db import Model

class Remind(Model):
    __tablename__ = 'reminds'
    
    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT, nullable=False)
    question_id = Column('question_id', INT, nullable=False)
    question_title = Column('question_title', VARCHAR(10), nullable=False)
    answer_id = Column('answer_id', INT, nullable=False)
    answer_content = Column('answer_content', VARCHAR(10), nullable=False)
    comment_id = Column('comment_id', INT, nullable=False)
    comment_content = Column('comment_content', VARCHAR(10), nullable=False)
    has_read = Column('has_read', Boolean, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    def __init__(self, user_id, question_id, question_title, answer_id, answer_content, comment_id, comment_content,  has_read=0):
        self.user_id = user_id
        self.question_id = question_id
        self.question_title = question_title[0:10]
        self.answer_id = answer_id
        self.answer_content = answer_content[0:10]
        self.comment_id = comment_id
        self.comment_content = comment_content[0:10]
        self.has_read = has_read
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Remind %d,%d>' % (self.user_id, self.question_id)
