# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request
from flask.ext.login import login_required, current_user

from odd.utils.error import *

from odd.biz.tag import *
from odd.biz.question import *

mod = Blueprint('search', __name__, url_prefix='/search')

@mod.route('/')
def index():
    args = request.args
    tag = args.getlist('tag')
    if not tag:
        return abort(404)

    tag_obj = get_tag_by_tag(tag[0])
    questions = get_question_by_tag(tag[0])
    return render_template('search/index.html', tag=tag_obj, questions=questions)

@mod.route('/tip')
def tip():
    tags = get_all_tags()
    ts = [t.tag for t in tags]
    return jsonify(errno='SUCCESS', tags=ts)

@mod.route('/tag')
def tag():
    tags = get_all_tags()
    ts = []
    for t in tags:
        ts.append({
            'id': t.id,
            'tag': t.tag,
            'photo': t.tag_photo(20)
            })
    return jsonify(errno='SUCCESS', tags=ts)
