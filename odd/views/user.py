# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort
from flaskext.login import login_required, current_user
from flaskext.wtf import Form, TextField, PasswordField, Required

from odd.utils.error import *

from odd.biz.user import *
from odd.biz.question import *

from functools import wraps

mod = Blueprint('user', __name__, url_prefix='/user')

@mod.route('/<nickname>')
@login_required
def index(nickname):
    if current_user.nickname == nickname:
        tags = [tf.tag for tf in current_user.tag_follows]
        questions = get_question_by_tags(tags)
        qs = order_by_time(questions)
        return render_template('user/index.html', questions=qs)

    user = get_user_by_name(nickname)
    if not user:
        abort(404)

    return render_template('user/main.html', user=user)
