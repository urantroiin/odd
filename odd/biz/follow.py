# -*- coding: utf-8 -*-

from odd.data.db import db_session
from odd.models.follow import *

from odd.utils.error import *

def new_tag_follow(tag_follow):
    db_session.add(tag_follow)
    db_session.commit()
    return TAG_FOLLOW_ADD_OK
