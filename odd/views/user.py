# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request
from flask.ext.login import login_required, current_user
from flaskext.wtf import Form, TextField, RadioField, FileField, Required, Email, Regexp

from odd.utils.error import *
from odd.utils.tools import *

from odd import app
from odd.biz.user import *
from odd.biz.question import *
from odd.biz.resource import *

from functools import wraps

mod = Blueprint('user', __name__)

@mod.route('/user/<nickname>')
@login_required
def index(nickname):
    user = get_user_by_name(nickname)
    if not user:
        abort(404)

    return render_template('user/index.html', user=user)

@mod.route('/followed')
@login_required
def followed():
    tags = [tf.tag for tf in current_user.tag_follows]

    questions = get_question_by_tags(tags)
    resources = get_resource_by_tags(tags)

    return render_template('user/home.html', nav_item='followed', questions=questions, resources=resources)

@mod.route('/my')
@login_required
def my():

    questions = get_question_by_uid(current_user.id)
    resources = get_resource_by_uid(current_user.id)

    return render_template('user/home.html', nav_item='my', questions=questions, resources=resources)

@mod.route('/around')
@login_required
def around():

    questions = get_latest_questions(20)
    questions = [q for q in questions if q.user_id != current_user.id]
    resources = get_latest_resources(20)
    resources = [r for r in resources if r.user_id != current_user.id]

    return render_template('user/home.html', nav_item='around', questions=questions, resources=resources)

@mod.route('/home')
@login_required
def home():
    return followed()

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
        save_photo(current_user.id, form.photo_img.data)

    success(ret)
    return render_template('user/profile.html', form=form)

class ProfileForm(Form):
    photo_img = FileField(u'头像', validators=[])
    email = TextField(u'邮箱地址*', validators=[Required(), Email()])
    nickname = TextField(u'昵称*', validators=[Required(),Regexp('[\w\d-]{2,20}')])
    title = TextField(u'签名*', validators=[Required(),Regexp('.{0,128}')])
    sex = RadioField(u'性别*', coerce=int, choices=[(0,u'男人'),(1,u'女人')])
