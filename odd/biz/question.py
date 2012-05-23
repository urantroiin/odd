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
    if not questions:
        return []

    uids = [q.user_id for q in questions]
    users = db_session.query(User).filter(User.id.in_(uids)).all()
    tags = db_session.query(Question_Tag).filter(Question_Tag.question_id.in_(ids)).all()
    for q in questions:
        for u in users:
            if u.id == q.user_id:
                q.user = u
                break
        q.tags = [tag.tag for tag in tags if tag.question_id==q.id]
    return questions

def get_question_by_id(id):
    questions = get_question_by_ids([id])
    if not questions:
        return None
    
    return questions[0]

def get_question_by_tags(tags):
    tags = db_session.query(Question_Tag).filter(Question_Tag.tag.in_(tags)).all()
    if not tags:
        return []

    ids = [t.question_id for t in tags]
    questions = get_question_by_ids(ids)
    return questions

def get_question_by_tag(tag):
    return get_question_by_tags([tag])

def new_question(question):
    db_session.add(question)
    db_session.commit()
    return QUESTION_ADD_OK
