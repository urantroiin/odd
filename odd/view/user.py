# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import  url_for, redirect, render_template 
from flaskext.login import login_required, current_user
from flaskext.wtf import Form, TextField, PasswordField, Required

from odd.util.error import *

from odd.biz.user import *

mod = Blueprint('user', __name__)

@mod.route('/<id>')
def index(id):
    return render_template('user/index.html', id=id)
