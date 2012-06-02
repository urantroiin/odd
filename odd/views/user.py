# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request
from flask.ext.login import login_required, current_user
from flaskext.wtf import Form, TextField, RadioField, FileField, Required, Email, Regexp

from odd.utils.error import *
from odd.utils.tools import *

from odd import app
from odd.biz.user import *
from odd.biz.question import *

from functools import wraps

mod = Blueprint('user', __name__)

@mod.route('/user/<nickname>')
@login_required
def index(nickname):
    user = get_user_by_name(nickname)
    if not user:
        abort(404)

    return render_template('user/index.html', user=user)

@mod.route('/home')
@login_required
def home():
    tags = [tf.tag for tf in current_user.tag_follows]
    followed = get_question_by_tags(tags)
    my = get_question_by_uid(current_user.id)
    latest = get_latest_questions(20)
    return render_template('user/home.html', followed=followed, my=my, latest=latest)

@mod.route('/profile', methods=['GET','POST'])
@login_required
def profile():
    form = ProfileForm(obj=current_user)
    if not form.validate_on_submit():
        return render_template('user/profile.html', form=form)

    form.populate_obj(current_user)

    ret = edit_user(current_user)
    if not ret == USER_EDIT_OK:
        fail(ret)
        return render_template('user/profile.html', form=form)

    if form.photo_img.data:
        save_img(current_user.id, form.photo_img.data)

    success(ret)
    return render_template('user/profile.html', form=form)

class ProfileForm(Form):
    photo_img = FileField(u'头像', validators=[])
    email = TextField(u'邮箱地址*', validators=[Required(), Email()])
    nickname = TextField(u'昵称*', validators=[Required()])
    title = TextField(u'签名*', validators=[Required()])
    sex = RadioField(u'性别*', coerce=int, choices=[(0,u'男人'),(1,u'女人')])
