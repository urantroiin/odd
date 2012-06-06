# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.tag import *

from odd.utils.error import *

def get_tag_by_id(id):
    return db_session.query(Tag).filter_by(id=id).first()

def get_all_tags():
    return db_session.query(Tag).all()

def get_tag_by_tag(tag):
    return db_session.query(Tag).filter_by(tag=tag).first()

def get_tag_by_page(page, count):
    return db_session.query(Tag).limit(count).offset(page*count).all()

def new_tags(tags):
    for tag in tags:
        try:
            db_session.add(tag)
            db_session.commit()
        except:
            db_session.rollback()

    return TAG_ADD_OK

def new_tag_edit(tag_edit):
    db_session.add(tag_edit)
    db_session.commit()
    return TAG_EDIT_ADD_OK
