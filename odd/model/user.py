# -*- coding: utf-8 -*-

from odd.data.db import Model
from flaskext.login import UserMixin

from sqlalchemy.schema import Column
from sqlalchemy.types import INT, VARCHAR, TIMESTAMP

from datetime import datetime
from hashlib import md5

class User(Model, UserMixin):
    __tablename__ = 'users'
    
    id = Column('id', INT, primary_key=True)
    email = Column('email', VARCHAR(50), unique=True, nullable=False)
    nickname = Column('nickname', VARCHAR(32), nullable=False)
    passwd = Column('passwd', VARCHAR(50), nullable=False)
    create_time = Column('create_time', TIMESTAMP, nullable=False)

    def __init__(self, email, passwd, nickname=''):
        self.email = email
        self.passwd = md5(passwd).hexdigest()
        self.nickname = nickname
        self.create_time = datetime.now()

    def email_hash(self):
        return md5(self.email.lower()).hexdigest()

    def __repr__(self):
        return '<User %r>' % self.email
