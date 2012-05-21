# -*- coding: utf-8 -*-

from flaskext.login import logout_user, login_user

from odd.data.db import db_session
from odd.model.user import User

from odd.util.error import *

def get_user_by_id(id):
    user = db_session.query(User).filter_by(id=id).first()
    return user

def get_all_users():
    users = db_session.query(User).filter_by(is_team=False).all()
    return users

def get_users_map():
    users = get_all_users()
    user_map = {}
    for u in users:
        user_map[u.username] = u.realname 
    return user_map

def get_user_by_email(email):
    user = db_session.query(User).filter_by(email=email).first()
    return user

def register(user):
    if get_user_by_email(user.email):
        return USER_DUPLICATE

    db_session.add(user)
    db_session.commit()
    return USER_ADD_OK

def edit_user(user):
    db_session.add(user)
    db_session.commit()
    return USER_EDIT_OK

def login(user):
    passwd = md5(user.passwd).hexdigest()
    u = db_session.query(User).filter_by(email=user.email, passwd=passwd).first()
    
    if not u:
        return USER_NOT_EXIST

    user.id = u.id
    login_user(u)

    return USER_LOGIN_OK

def logout():
    logout_user()
    return USER_LOGOUT_OK
