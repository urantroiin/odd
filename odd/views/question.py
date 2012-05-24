# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flaskext.login import login_required, current_user
from flaskext.wtf import Form, TextField, TextAreaField, HiddenField, Required

from odd.utils.error import *

from odd.models.question import *
from odd.biz.question import *

from functools import wraps

from re import match

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

@mod.route('/answer', methods=['POST'])
@login_required
def answer():
    form = request.form
    question_id = form.getlist('question_id')
    content = form.getlist('content')
    if not question_id or not content:
        return jsonify(errno='FAIL')

    answer = Answer(current_user.id, question_id[0], content[0])
    ret = new_answer(answer)
    if ret != ANSWER_ADD_OK:
        return jsonify(errno='FAIL')

    return jsonify(errno='SUCCESS')

@mod.route('/up', methods=['POST'])
@login_required
def up():
    form = request.form
    answer_id = form.getlist('answer_id')
    if not answer_id:
        return jsonify(errno='FAIL')

    up = Up(current_user.id, answer_id[0])
    ret = new_up(up)
    if ret != UP_ADD_OK:
        return jsonify(errno='FAIL')

    return jsonify(errno='SUCCESS')

@mod.route('/comment', methods=['POST'])
@login_required
def comment():
    form = request.form
    answer_id = form.getlist('answer_id')
    comment_id = form.getlist('comment_id')
    content = form.getlist('content')
    if not answer_id or not comment_id or not content:
        return jsonify(errno='FAIL')

    comm = Comment(current_user.id, answer_id[0], comment_id[0], content[0])
    ret = new_comment(comm)
    if ret != COMMENT_ADD_OK:
        return jsonify(errno='FAIL')

    return jsonify(errno='SUCCESS')



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

class AnswerForm(Form):
    question_id = HiddenField(validators=[Required])
    content = TextAreaField(u'内容', validators=[Required()])
