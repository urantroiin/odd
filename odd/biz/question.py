# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.question import *
from odd.models.tag import *
from odd.biz.tag import new_tags

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

def get_question_gt_id(id,count):
    questions = db_session.query(Question).filter(Question.id>id).order_by(Question.id).limit(count).all()
    return questions

def get_latest_questions(count):
    questions = db_session.query(Question).order_by(Question.id.desc()).limit(count).all()
    return questions

def get_question_by_time(time):
    questions = db_session.query(Question).filter(Question.create_time>time).all()
    return questions

def get_question_by_tags(tags):
    tags = db_session.query(Question_Tag).filter(Question_Tag.tag.in_(tags)).order_by(Question_Tag.id.desc()).all()
    qs = []
    for t in tags:
        if not t.question in qs:
            qs.append(t.question)
    return qs

def get_question_by_uid(uid):
    questions = db_session.query(Question).filter_by(user_id=uid).order_by(Question.id.desc()).all()
    return questions

def get_question_titles(count):
    questions = db_session.query(Question.id, Question.title).order_by(Question.id.desc()).limit(count).all()
    return questions

def get_question_by_tag(tag):
    tags = db_session.query(Question_Tag).filter_by(tag=tag).all()
    return [t.question for t in tags]

def new_question(question, tags):
    db_session.begin()
    new_tags(tags)

    db_session.add(question)
    db_session.commit()

    return QUESTION_ADD_OK

def edit_question(question, tags):
    db_session.begin()
    new_tags(tags)

    db_session.add(question)
    db_session.commit()

    return QUESTION_EDIT_OK

def edit_question_tags(qid, tags):
    db_session.begin()
    new_tags(tags)

    db_session.query(Question_Tag).filter_by(question_id=qid).delete()
    db_session.add_all([Question_Tag(qid,tag) for tag in tags])
    db_session.commit()
    return QUESTION_TAG_EDIT_OK

def new_question_edit(question_edit):
    db_session.begin()
    db_session.add(question_edit)
    db_session.commit()
    return QUESTION_EDIT_ADD_OK
