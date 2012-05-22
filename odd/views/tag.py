# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort 
from flaskext.login import login_required, current_user
from flaskext.wtf import Form, TextField, PasswordField, Required

from odd.utils.error import *

from odd.biz.tag import *

from functools import wraps

def check_load_tag(func):
    @wraps(func)
    def wrapper(**kv):
        if 'name' in kv.keys():
            tag = get_tag_by_name(kv['name'])
       
        if tag:
            return func(tag=tag, **kv)
        else:
            return abort(404)

    return wrapper

mod = Blueprint('tag', __name__)

@mod.route('/<name>')
@login_required
@check_load_tag
def index(tag, **kv):
    return render_template('group/index.html', tag=tag)
