# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flask.ext.login import login_required, current_user

from odd import app

from odd.utils.error import *

from odd.biz.tag import *
from odd.biz.question import *
from odd.biz.resource import *

mod = Blueprint('admin', __name__, url_prefix='/admin')

@mod.route('/')
@login_required
def index():
    if not current_user.nickname in app.config['ADMINS']:
        abort(404)
    return render_template('admin/index.html')
