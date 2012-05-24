# -*- coding: utf-8 -*-

from odd.data.db import Model

from sqlalchemy.orm import relation, backref
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP, TEXT

from datetime import datetime

class Question(Model):
    __tablename__ = 'questions'
    
    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT, ForeignKey('users.id'), nullable=False)
    title = Column('title', VARCHAR(255), nullable=False)
    content = Column('content', TEXT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)
    
    user = relation("User")
    tags = relation("Question_Tag", backref=backref('question'))
    answers = relation("Answer")

    def __init__(self, user_id, title, content):
        self.user_id = user_id
        self.title = title
        self.content = content
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Question %r>' % self.title

class Answer(Model):
    __tablename__ = 'answers'
    
    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT, ForeignKey('users.id'), nullable=False)
    question_id = Column('question_id', INT, ForeignKey('questions.id'), nullable=False)
    content = Column('content', TEXT, nullable=False)
    up = Column('up', INT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)
    
    user = relation("User")
    comments = relation("Comment")

    def __init__(self, user_id, question_id, content, up=0):
        self.user_id = user_id
        self.question_id = question_id
        self.content = content
        self.up = up
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Answer %d,%d>' % (self.user_id, self.question_id)

class Up(Model):
    __tablename__ = 'ups'

    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT,  nullable=False)
    answer_id = Column('answer_id', INT,  nullable=False)

    def __init__(self, user_id, answer_id):
        self.user_id = user_id
        self.answer_id = answer_id

    def __repr__(self):
        return '<Up %d,%d>' % (self.user_id, self.answer_id)

class Comment(Model):
    __tablename__ = 'comments'
    
    id = Column('id', INT, primary_key=True)
    user_id = Column('user_id', INT, ForeignKey('users.id'), nullable=False)
    answer_id = Column('answer_id', INT, ForeignKey('answers.id'), nullable=False)
    comment_id = Column('comment_id', INT, nullable=False)
    content = Column('content', TEXT, nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)
    
    user = relation("User")

    def __init__(self, user_id, answer_id, comment_id, content):
        self.user_id = user_id
        self.answer_id = answer_id
        self.comment_id = comment_id
        self.content = content
        self.create_time = datetime.now()

    def __repr__(self):
        return '<Comment %d,%d>' % (self.user_id, self.answer_id)
