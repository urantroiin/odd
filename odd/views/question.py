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

    args = request.args
    answer_id = args.getlist('answer_id')[0] if args.getlist('answer_id') else -1
    comment_id = args.getlist('comment_id')[0] if args.getlist('comment_id') else -1

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
    qid = request.args.getlist('qid')
    if not qid:
        return jsonify(errno='FAIL')
    
    count = request.args.getlist('count')
    if not count:
        return jsonify(errno='FAIL')

    ques = get_question_gt_id(qid[0], count[0])
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


@mod.route('/new', methods=['GET','POST'])
@login_required
def new():

    form = NewQueForm()
    if not form.validate_on_submit():
        return render_template('question/new.html', form=form)

    title = form.title.data
    content = form.content.data

    tags = request.form.getlist('tag')
    tags_clean = []
    for t in tags:
        t = t.strip()
        if t and t not in tags_clean:
            tags_clean.append(t)

    question = Question(current_user.id, title, content, tags_clean)
    ret = new_question(question, tags_clean)
    if ret != QUESTION_ADD_OK:
        fail(ret)
        return render_template('question/new.html', form=form)

    return redirect(url_for('.index', id=question.id))

class NewQueForm(Form):
    title = TextField(u'标题*', validators=[Required()])
    content = TextAreaField(u'内容*', validators=[Required()])
    tags = TextField(u'标签*')
