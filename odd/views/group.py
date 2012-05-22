# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import  url_for, redirect, render_template 
from flaskext.login import login_required, current_user
from flaskext.wtf import Form, TextField, PasswordField, Required

from odd.utils.error import *

from odd.biz.group import *

from functools import wraps

def check_load_group(func):
    @wraps(func)
    def wrapper(**kv):
        if 'name' in kv.keys():
            group = get_group_by_name(kv['name'])
       
        if group:
            return func(group=group, **kv)
        else:
            return abort(404)

    return wrapper

mod = Blueprint('group', __name__)

@mod.route('/<name>')
@check_load_group
def index(group, **kv):
    return render_template('group/index.html', group=group)
