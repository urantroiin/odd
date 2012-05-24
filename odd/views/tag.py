# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request
from flaskext.login import login_required, current_user

from odd.utils.error import *

from odd.biz.question import *

mod = Blueprint('tag', __name__, url_prefix='/tag')

@mod.route('/<tag>')
@login_required
def index(tag):
    questions = get_question_by_tag(tag)
    return render_template('tag/index.html', tag=tag, questions=questions)
