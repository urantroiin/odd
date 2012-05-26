# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flaskext.login import login_required, current_user

from odd.utils.error import *

from odd.biz.answer import *
from odd.biz.remind import *

from functools import wraps

from re import match

mod = Blueprint('answer', __name__, url_prefix='/question/answer')

@mod.route('/new', methods=['POST'])
@login_required
def new():
    form = request.form
    question_id = form.getlist('question_id')
    content = form.getlist('content')
    if not question_id or not content:
        return jsonify(errno='FAIL')

    answer = Answer(current_user.id, question_id[0], content[0])
    ret = new_answer(answer)
    if ret != ANSWER_ADD_OK:
        return jsonify(errno='FAIL')

    remind = Remind(answer.question.user.id, question_id[0], answer.id, -1)
    new_remind(remind)

    return jsonify(errno='SUCCESS')

@mod.route('/up', methods=['POST'])
@login_required
def up():
    form = request.form
    answer_id = form.getlist('answer_id')
    if not answer_id:
        return jsonify(errno='FAIL')

    answer_up = Answer_Up(current_user.id, answer_id[0])
    ret = new_answer_up(answer_up)
    if ret != ANSWER_UP_ADD_OK:
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

    user_id = comm.comment.user.id if comm.comment else comm.answer.user.id
    remind = Remind(user_id, comm.answer.question.id, -1, comm.id)
    new_remind(remind)

    return jsonify(errno='SUCCESS')
