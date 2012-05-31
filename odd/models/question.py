# -*- coding: utf-8 -*-

from datetime import datetime

from sqlalchemy.orm import relation, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP, TEXT

from odd.data.db import Model

from odd.models.answer import Answer

class Question(Model):
    __tablename__ = 'questions'
    
    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT, ForeignKey('users.id'), nullable=False)
    title = Column('title', VARCHAR(255), nullable=False)
    content = Column('content', TEXT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)
    answer_count = Column('answer_count', INT, nullable=False)
    
    user = relation("User")
    tags = relation("Question_Tag", backref=backref('question'))
    answers = relation("Answer", order_by='desc(Answer.up)', backref=backref('question'))

    def __init__(self, user_id, title, content, tags):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.tags = [Question_Tag(self.id, tag) for tag in tags]
        self.create_time = datetime.now()
        self.answer_count = 0

    def __repr__(self):
        return '<Question %r>' % self.title

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
