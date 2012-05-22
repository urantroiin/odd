# -*- coding: utf-8 -*-

from odd.data.db import db_session
from odd.models.question import *

from odd.utils.error import *

def get_question_by_id(id):
    question = db_session.query(Question).filter_by(id=id).first()
    return question

def get_question_by_name(name):
    question = db_session.query(Question).filter_by(name=name).first()
    return question

def new_question(question):
    db_session.add(question)
    db_session.commit()
    return QUESTION_ADD_OK

def new_question_tags(question_tags):
    for qt in question_tags:
        db_session.add(qt)
    db_session.commit()
    return QUESTION_TAG_ADD_OK

def get_question_tags(question_id):
    question_tags = db_session.query(Question_Tag).filter_by(question_id=question_id).all()
    return question_tags

