# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flask.ext.login import login_required, current_user

from odd.utils.error import *

from odd.biz.remind import *

mod = Blueprint('remind', __name__, url_prefix='/remind')

@mod.route('/', methods=['GET'])
@login_required
def index():
    reminds = get_unread_reminds(current_user.id)
    rdicts = []
    for r in reminds:
        rdicts.append({
            'id': r.id,
            'type': 'answer' if r.comment_id==-1 else 'comment',
            'question': r.question_title,
            'answer': r.answer_content,
            'comment': r.comment_content
            })
    return jsonify(errno='SUCCESS', reminds = rdicts)

@mod.route('/read', methods=['GET'])
@login_required
def read():
    args = request.args
    id = args.get('id')
    if not id:
        return abort(404)
    
    remind = get_remind_by_id(id)
    remind.has_read = True
    edit_remind(remind)
    
    return redirect(url_for('question.index', id=remind.question_id, answer_id=remind.answer_id, comment_id=remind.comment_id))
