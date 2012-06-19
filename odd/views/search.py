# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flask.ext.login import login_required, current_user

from odd.utils.error import *

from odd.biz.tag import *
from odd.biz.question import *
from odd.biz.resource import *

mod = Blueprint('search', __name__, url_prefix='/search')

@mod.route('/')
def index():
    args = request.args
    tag = args.get('tag')
    if not tag:
        return abort(404)

    tag_obj = get_tag_by_tag(tag)
    questions = get_question_by_tag(tag)
    return render_template('search/index.html', tag=tag_obj, questions=questions)

@mod.route('/tips')
def tips():
    tags = get_all_tags()
    ts = []
    for t in tags:
        ts.append({
            'id': t.id,
            'tag': t.tag,
            'photo': t.tag_photo(20)
            })

    questions = get_question_titles(100)
    qs = []
    for q in questions:
        qs.append({
            'id': q.id,
            'title': q.title,
            })
    
    resources = get_resource_titles(100)
    rs = []
    for r in resources:
        rs.append({
            'id': r.id,
            'title': r.title,
            })

    return jsonify(errno='SUCCESS', tags=ts, questions=qs, resources=rs)
