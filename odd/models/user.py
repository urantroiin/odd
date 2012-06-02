# -*- coding: utf-8 -*-

from datetime import datetime
from hashlib import md5

from flask.ext.login import UserMixin

from sqlalchemy.orm import relation
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP, BOOLEAN

from odd.data.db import Model

from odd.models.follow import *

class User(Model, UserMixin):
    __tablename__ = 'users'
    
    id = Column('id', INT, primary_key=True)
    email = Column('email', VARCHAR(50), unique=True, nullable=False)
    nickname = Column('nickname', VARCHAR(32), nullable=False)
    title = Column('title', VARCHAR(128), nullable=False)
    sex = Column('sex', BOOLEAN, nullable=False)
    passwd = Column('passwd', VARCHAR(50), nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    tag_follows = relation('Tag_Follow')

    def __init__(self, email, passwd, nickname=''):
        self.email = email
        self.passwd = md5(passwd).hexdigest()
        self.nickname = nickname
        self.create_time = datetime.now()

    def email_hash(self):
        return md5(self.email.lower()).hexdigest() 

    def photo(self,size):
        return join(app.config['PHOTO_PATH'], '%d-%d.jpg' % (self.id, size))

    def tag_is_followed(self, tag):
        tags = [tf.tag for tf in self.tag_follows]
        return tag in tags

    def __repr__(self):
        return '<User %r>' % self.email
