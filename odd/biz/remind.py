# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.remind import *

from odd.utils.error import *

def get_remind_by_id(id):
    remind = db_session.query(Remind).get(id)
    return remind

def get_unread_reminds(uid):
    reminds = db_session.query(Remind).filter_by(user_id=uid, has_read=False).all()
    return reminds

def new_remind(remind):
    db_session.begin()
    db_session.add(remind)
    db_session.commit()
    return REMIND_ADD_OK

def edit_remind(remind):
    db_session.begin()
    db_session.add(remind)
    db_session.commit()
    return REMIND_EDIT_OK
