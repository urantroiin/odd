# -*- coding: utf-8 -*-

from odd.data.db import db_session
from odd.models.group import Group

from odd.utils.error import *

def get_group_by_id(id):
    group = db_session.query(Group).filter_by(id=id).first()
    return group
