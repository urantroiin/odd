# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request
from flaskext.login import login_required, current_user
from flaskext.wtf import Form, TextField, TextAreaField, PasswordField, Required

from odd.utils.error import *

from odd.models.question import *
from odd.biz.question import *

from functools import wraps

def check_load_question(func):
    @wraps(func)
    def wrapper(**kv):
        if 'id' in kv.keys():
            question = get_question_by_id(kv['id'])
       
        if question:
            return func(question=question, **kv)
        else:
            return abort(404)

    return wrapper

mod = Blueprint('question', __name__, url_prefix='/question')

@mod.route('/<id>')
@login_required
def index(id):
    question = get_question_by_id(id)
    if not question:
        abort(404)
    return render_template('question/index.html', question=question)


@mod.route('/new', methods=['GET','POST'])
@login_required
def new():

    form = NewQueForm()
    if not form.validate_on_submit():
        return render_template('question/new.html', form=form)

    title = form.title.data
    content = form.content.data

    question = Question(current_user.id, title, content)
    ret = new_question(question)
    if ret != QUESTION_ADD_OK:
        fail(ret)
        return render_template('question/new.html', form=form)

    tags = set(form.tags.data.split(' '))

    question_tags = [Question_Tag(question.id, tag) for tag in tags if tag]
    ret = new_question_tags(question_tags)
    if ret != QUESTION_TAG_ADD_OK:
        fail(ret)
        return render_template('question/new.html', form=form)

    return redirect(url_for('.index', id=question.id))

class NewQueForm(Form):
    title = TextField(u'标题', validators=[Required()])
    content = TextAreaField(u'内容', validators=[Required()])
    tags = TextField(u'标签', validators=[Required()])
