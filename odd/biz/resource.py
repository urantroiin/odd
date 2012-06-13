# -*- coding: utf-8 -*-

from odd.data.db import db_session

from odd.models.resource import *
from odd.models.tag import *

from odd.biz.tag import *

from odd.utils.error import *

def get_resource_by_id(id):
    resource = db_session.query(Resource).get(id)
    return resource

def get_resource_by_tag(tag):
    tags = db_session.query(Resource_Tag).filter_by(tag=tag).all()
    return [t.resource for t in tags]

def get_latest_resources(count):
    resources = db_session.query(Resource).order_by(Resource.id.desc()).limit(count).all()
    return resources

def new_resource(resource, tags):
    new_tags([Tag(tag) for tag in tags])

    db_session.add(resource)
    db_session.commit()

    return RESOURCE_ADD_OK

def new_resource_download(rd):
    download = db_session.query(Resource_Download).filter_by(resource_id=rd.resource_id, 
            user_id=rd.user_id).first()
    if download:
        return RESOURCE_DOWNLOAD_DUPLICATE
    
    db_session.add(rd)

    resource = db_session.query(Resource).get(rd.resource_id)
    resource.download_count += 1
    
    db_session.commit()
    return RESOURCE_DOWNLOAD_ADD_OK
