# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flaskext.login import login_required, current_user

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
            'question': r.question.title[0:10],
            'answer': r.answer.content[0:10] if r.answer else False,
            'comment': r.comment.content[0:10] if r.comment else False
            })
    return jsonify(errno='SUCCESS', reminds = rdicts)

@mod.route('/read', methods=['GET'])
@login_required
def read():
    args = request.args
    id = args.getlist('id')
    if not id:
        return abort(404)
    
    remind = get_remind_by_id(id[0])
    remind.has_read = True
    edit_remind(remind)
    
    if remind.comment:
        return redirect(url_for('question.index', id=remind.question.id))
    else:
        return redirect(url_for('question.index', id=remind.question.id))
