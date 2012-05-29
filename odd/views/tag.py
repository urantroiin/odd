# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flask.ext.login import login_required, current_user

from odd.utils.error import *

from odd.biz.question import *

mod = Blueprint('tag', __name__, url_prefix='/tag')

@mod.route('/')
@login_required
def all():
    tags = get_question_tags()
    return jsonify(errno='SUCCESS', tags=tags)


@mod.route('/<tag>')
@login_required
def index(tag):
    questions = get_question_by_tag(tag)
    return render_template('tag/index.html', tag=tag, questions=questions)

@mod.route('/list')
@login_required
def list():
    return render_template('tag/list.html')
