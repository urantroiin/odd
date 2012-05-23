# -*- coding: utf-8 -*-

from odd.data.db import db_session
from odd.models.question import *
from odd.models.tag import *
from odd.models.user import *

from odd.biz.tag import *

from odd.utils.error import *

def get_question_by_ids(ids):
    '''
    输入问题ID数组
    输出问题数组
    '''
    questions = db_session.query(Question).filter(Question.id.in_(ids)).all()
    return questions

def get_question_by_id(id):
    question = db_session.query(Question).filter_by(id=id).first()
    return question

def get_question_by_tags(tags):
    tags = db_session.query(Question_Tag).filter(Question_Tag.tag.in_(tags)).all()
    return [t.question for t in tags]

def get_question_by_tag(tag):
    tags = db_session.query(Question_Tag).filter_by(tag=tag).all()
    return [t.question for t in tags]

def new_question(question):
    db_session.add(question)
    db_session.commit()
    return QUESTION_ADD_OK

def new_answer(answer):
    db_session.add(answer)
    db_session.commit()
    return QUESTION_ADD_OK
