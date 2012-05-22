# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort
from flaskext.login import login_required, current_user
from flaskext.wtf import Form, TextField, PasswordField, Required

from odd.utils.error import *

from odd.biz.user import *

from functools import wraps

def check_load_user(func):
    @wraps(func)
    def wrapper(**kv):
        if 'nickname' in kv.keys():
            user = get_user_by_name(kv['nickname'])
        else:
            user = current_user
       
        if user:
            return func(user=user, **kv)
        else:
            return abort(404)

    return wrapper

mod = Blueprint('user', __name__)

@mod.route('/<nickname>')
@login_required
@check_load_user
def index(user, **kv):
    return render_template('user/index.html', user=user)
