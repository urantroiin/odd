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
    query = request.args.get('query')
    if not query:
        abort(404)

    query = query.lower()

    count = 50

    tags = [t for t in get_latest_tags(count) if query in t.tag.lower()]
    questions = [q for q in get_latest_questions(count) if query in q.title.lower()]
    resources = [r for r in get_latest_resources(count) if query in r.title.lower()]

    return render_template('search/index.html', tags=tags, questions=questions, resources=resources)

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
