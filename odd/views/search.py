# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request
from flaskext.login import login_required, current_user

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

    questions = get_question_by_tag(tag[0])
    return render_template('search/index.html', tag=tag[0], questions=questions)
