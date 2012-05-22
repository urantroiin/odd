# -*- coding: utf-8 -*-

from odd.data.db import db_session
from odd.models.tag import Tag

from odd.utils.error import *

def get_tag_by_id(id):
    tag = db_session.query(Tag).filter_by(id=id).first()
    return tag

def get_tag_by_name(name):
    tag = db_session.query(Tag).filter_by(name=name).first()
    return tag
