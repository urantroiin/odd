# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flask.ext.login import login_required, current_user

from odd.utils.error import *
from odd.utils.tools import *

from odd.models.tag import *

from odd.biz.tag import *
from odd.biz.question import *
from odd.biz.resource import *

mod = Blueprint('tag', __name__, url_prefix='/tag')

@mod.route('/obj')
def obj():
    tags = get_all_tags()
    ts = []
    for t in tags:
        ts.append({
            'id': t.id,
            'tag': t.tag,
            'photo': t.tag_photo(20)
            })
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

@mod.route('/<int:id>/photo', methods=['POST'])
@login_required
def photo(id):
    tag_photo = request.files['tag_photo']
    if not tag_photo:
        return jsonify(errno='FAIL')
    
    save_tag_photo(id, tag_photo)

    tag_edit = Tag_Edit(current_user.id, id, '', 1)
    new_tag_edit(tag_edit)

    return jsonify(errno='SUCCESS')
    

@mod.route('/<int:id>/desc', methods=['POST'])
@login_required
def desc(id):
    desc = request.form.get('desc')
    if not desc:
        return jsonify(errno='FAIL')

    tag_obj = get_tag_by_id(id)
    tag_obj.description = desc
    ret = edit_tag(tag_obj)
    if ret != TAG_EDIT_OK:
        return jsonify(errno='FAIL')
        
    tag_edit = Tag_Edit(current_user.id, id, desc, -1)
    new_tag_edit(tag_edit)

    return jsonify(errno='SUCCESS')
