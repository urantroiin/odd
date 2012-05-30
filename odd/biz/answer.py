# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.answer import *
from odd.models.question import *

from odd.utils.error import *

def new_answer(answer):
    db_session.add(answer)

    question = db_session.query(Question).get(answer.question_id)
    question.answer_count += 1
    
    db_session.commit()
    return ANSWER_ADD_OK


def new_answer_up(answer_up):
    au = db_session.query(Answer_Up).filter_by(answer_id=answer_up.answer_id, 
            user_id=answer_up.user_id).first()
    if au:
        return ANSWER_UP_DUPLICATE

    db_session.add(answer_up)

    anwser = db_session.query(Answer).get(answer_up.answer_id)
    anwser.up += 1

    db_session.commit()
    
    return ANSWER_UP_ADD_OK

def new_comment(comment):
    db_session.add(comment)
    db_session.commit()
    return COMMENT_ADD_OK
