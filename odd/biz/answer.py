# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.answer import *

from odd.utils.error import *

def new_answer(answer):
    db_session.add(answer)
    db_session.commit()
    return ANSWER_ADD_OK

def new_answer_up(answer_up):
    try:
        db_session.add(answer_up)
        db_session.commit()
    
        anwser = db_session.query(Answer).get(answer_up.answer_id)
        anwser.up += 1
        db_session.commit()
        
        return ANSWER_UP_ADD_OK
    except:
        db_session.rollback()
        return ANSWER_UP_DUPLICATE

def new_comment(comment):
    db_session.add(comment)
    db_session.commit()
    return COMMENT_ADD_OK
