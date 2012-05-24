# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.question import *

from odd.utils.error import *

def get_question_by_ids(ids):
    '''
    输入问题ID数组
    输出问题数组
    '''
    questions = db_session.query(Question).get(set(ids))
    return questions

def get_question_by_id(id):
    question = db_session.query(Question).get(id)
    return question

def get_question_by_tags(tags):
    tags = db_session.query(Question_Tag).filter(Question_Tag.tag.in_(tags)).all()
    return set([t.question for t in tags])

def get_question_by_tag(tag):
    tags = db_session.query(Question_Tag).filter_by(tag=tag).all()
    return [t.question for t in tags]

def order_by_time(questions):
    def time_key(q):
        return q.create_time
    return questions.sort(key=time_key)

def new_question(question):
    db_session.add(question)
    db_session.commit()
    return QUESTION_ADD_OK

def new_question_tags(question_tags):
    for qt in question_tags:
        db_session.add(qt)
    db_session.commit()
    return QUESTION_TAG_ADD_OK
