# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flask.ext.login import login_required, current_user

from odd.utils.error import *

from odd.biz.tag import *
from odd.biz.question import *
from odd.biz.resource import *

mod = Blueprint('tag', __name__, url_prefix='/tag')

@mod.route('/')
@login_required
def all():
    tags = get_all_tags()
    ts = [t.tag for t in tags]
    return jsonify(errno='SUCCESS', tags=ts)


@mod.route('/<tag>')
@login_required
def index(tag):
    tag_obj = get_tag_by_tag(tag)
    if not tag_obj:
        abort(404)
    questions = get_question_by_tag(tag)
    resources = get_resource_by_tag(tag)
    return render_template('tag/index.html', tag=tag_obj, questions=questions, resources=resources)

@mod.route('/list')
@login_required
def list():
    tags = get_tag_by_page(0, 30)
    return render_template('tag/list.html', tags=tags)
