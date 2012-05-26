# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy.orm import relation, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, Boolean, TIMESTAMP

from odd.data.db import Model

class Remind(Model):
    __tablename__ = 'reminds'
    
    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT, ForeignKey('users.id'), nullable=False)
    question_id = Column('question_id', INT, ForeignKey('questions.id'), nullable=False)
    answer_id = Column('answer_id', INT, ForeignKey('answers.id'), nullable=False)
    comment_id = Column('comment_id', INT, ForeignKey('comments.id'), nullable=False)
    has_read = Column('has_read', Boolean, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    user = relation("User")
    question = relation("Question")
    answer = relation("Answer")
    comment = relation("Comment")

    def __init__(self, user_id, question_id, answer_id, comment_id, has_read=0):
        self.user_id = user_id
        self.question_id = question_id
        self.answer_id = answer_id
        self.comment_id = comment_id
        self.has_read = has_read
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Remind %d,%d>' % (self.user_id, self.question_id)
