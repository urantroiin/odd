# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.notice import *
from odd.models.tag import *

from odd.utils.error import *

def get_notice_by_id(id):
    notice = db_session.query(Notice).get(id)
    return notice

def get_notice_by_tag(tag):
    tags = db_session.query(Notice_Tag).filter_by(tag=tag).all()
    return [t.notice for t in tags]
