# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort
from flask.ext.login import login_required, current_user
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
        followed = get_question_by_tags(tags)
        my = get_question_by_uid(current_user.id)
        latest = get_latest_questions(20)
        return render_template('user/index.html', followed=followed, my=my, latest=latest)

    user = get_user_by_name(nickname)
    if not user:
        abort(404)

    return render_template('user/main.html', user=user)
