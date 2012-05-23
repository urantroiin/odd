# -*- coding: utf-8 -*-

from odd.data.db import db_session
from odd.models.tag import *

from odd.utils.error import *

def new_question_tags(question_tags):
    for qt in question_tags:
        db_session.add(qt)
    db_session.commit()
    return QUESTION_TAG_ADD_OK

def get_question_tag_by_qid(qids):
    tags = db_session.query(Question_Tag).filter(Question_Tag.question_id.in_(qids)).all()
    return tags

def get_question_tag_by_tag(tags):
    tags = db_session.query(Question_Tag).filter(Question_Tag.tag.in_(tags)).all()
    return tags
