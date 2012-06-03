# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.resource import *
from odd.models.tag import *

from odd.utils.error import *

def get_resource_by_id(id):
    resource = db_session.query(Resource).get(id)
    return resource

def get_resource_by_tag(tag):
    tags = db_session.query(Resource_Tag).filter_by(tag=tag).all()
    return [t.resource for t in tags]
