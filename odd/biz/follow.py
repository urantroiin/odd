# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.follow import *

from odd.utils.error import *

def new_tag_follow(tag_follow):
    tf = db_session.query(Tag_Follow).filter_by(user_id=tag_follow.user_id, tag=tag_follow.tag).first()
    if tf:
        return TAG_FOLLOW_DUPLICATE

    db_session.add(tag_follow)
    db_session.commit()
    return TAG_FOLLOW_ADD_OK

def del_tag_follow(tag_follow):
    db_session.query(Tag_Follow).filter_by(user_id=tag_follow.user_id,tag=tag_follow.tag).delete()
    db_session.commit()
    return TAG_FOLLOW_DEL_OK
