# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flask.ext.login import login_required, current_user
from flaskext.wtf import Form, TextField, TextAreaField, Required

from odd.utils.error import *

from odd.models.question import *
from odd.biz.question import *

from functools import wraps

from re import match

from datetime import datetime, timedelta

mod = Blueprint('question', __name__, url_prefix='/question')

@mod.route('/<id>')
@login_required
def index(id):
    question = get_question_by_id(id)
    if not question:
        abort(404)

    answer_id = request.args.get('answer_id', -1, type=int)
    comment_id = request.args.get('comment_id', -1, type=int)

    return render_template('question/index.html', question=question, answer_id=answer_id, comment_id=comment_id)

@mod.route('/list')
@login_required
def list():
    #dt = datetime.now()-timedelta(minutes=5)
    #latest_ques = get_question_by_time(dt.strftime('%Y-%m-%d %H:%M'))
    latest_ques = get_latest_questions(20)
    return render_template('question/list.html', latest_questions=latest_ques)

@mod.route('/latest')
def latest():
    qid = request.args.get('qid')
    if not qid:
        return jsonify(errno='FAIL')
    
    count = request.args.get('count')
    if not count:
        return jsonify(errno='FAIL')

    ques = get_question_gt_id(qid, count)
    qs = []
    for q in ques:
        qs.append({
            'id': q.id,
            'title': q.title,
            'create_time': q.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'answer_count': q.answer_count,
            'tags': [qt.tag for qt in q.tags]
            })
    return jsonify(errno='SUCCESS', questions=qs)

def clean_tags(tags):
    tags_clean = []
    for t in tags:
        t = t.strip()
        if t and t not in tags_clean:
            tags_clean.append(t)
    return tags_clean


@mod.route('/<int:id>/tags', methods=['POST'])
@login_required
def tags(id):
    tags = request.form.get('tags')
    if not tags:
        return jsonify(errno='FAIL')

    tags = clean_tags(tags.split(','))

    ret = edit_question_tags(id, tags)
    if ret != QUESTION_TAG_EDIT_OK:
        return jsonify(errno='FAIL')
    
    question_edit = Question_Edit(current_user.id, id, tags)
    new_question_edit(question_edit)

    return jsonify(errno='SUCCESS')

@mod.route('/new', methods=['GET','POST'])
@login_required
def new():

    form = NewQueForm()
    if not form.validate_on_submit():
        return render_template('question/new.html', form=form)

    title = form.title.data
    content = form.content.data
    tags = clean_tags(form.tags.data.split(','))

    question = Question(current_user.id, title, content, tags)
    ret = new_question(question, tags)
    if ret != QUESTION_ADD_OK:
        fail(ret)
        return render_template('question/new.html', form=form)

    return redirect(url_for('.index', id=question.id))



class NewQueForm(Form):
    title = TextField(u'标题*', validators=[Required()])
    content = TextAreaField(u'内容*', validators=[Required()])
    tags = TextField(u'标签*', validators=[Required()])
