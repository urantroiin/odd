# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.tag import *

from odd.utils.error import *

def new_tags(tags):
    db_session.add_all(tags)
    db_session.commit()
    return TAG_ADD_OK

def get_all_tags():
    return db_session.query(Tag).all()

