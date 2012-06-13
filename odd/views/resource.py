# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flask.ext.login import login_required, current_user
from flaskext.wtf import Form, TextField, FileField, FieldList, Required

from odd.utils.error import *
from odd.utils.tools import *

from odd.models.resource import *
from odd.biz.resource import *

mod = Blueprint('resource', __name__, url_prefix='/resource')

@mod.route('/<id>')
@login_required
def index(id):
    resource = get_resource_by_id(id)
    if not resource:
        abort(404)

    return render_template('resource/index.html', resource=resource)

@mod.route('/<id>/download', methods=['POST'])
@login_required
def download(id):
    resource = get_resource_by_id(id)
    if not resource:
        return jsonify(errno='FAIL')
    
    rd = Resource_Download(id, current_user.id)
    new_resource_download(rd)

    return jsonify(errno='SUCCESS')

@mod.route('/list')
@login_required
def list():
    latest_res = get_latest_resources(20)
    return render_template('resource/list.html', latest_resources=latest_res)

def clean_tags(tags):
    tags_clean = []
    for t in tags:
        t = t.strip()
        if t and t not in tags_clean:
            tags_clean.append(t)
    return tags_clean

@mod.route('/<int:id>/tags', methods=['POST'])
@login_required
def tags(id):
    tags = request.form.getlist('tags')
    if not tags:
        return jsonify(errno='FAIL')

    tags = clean_tags(tags[0].split(','))

    ret = edit_resource_tags(id, tags)
    if ret != QUESTION_TAG_EDIT_OK:
        return jsonify(errno='FAIL')
    
    resource_edit = Resource_Edit(current_user.id, id, tags)
    new_resource_edit(resource_edit)

    return jsonify(errno='SUCCESS')

def clean_files(files):
    files_clean = []
    for f in files:
        if f.filename:
            files_clean.append(f)
    return files

@mod.route('/new', methods=['GET','POST'])
@login_required
def new():

    form = NewResForm()
    files = clean_files(request.files.getlist('files'))

    if not files or not form.validate_on_submit():
        return render_template('resource/new.html', form=form)
    
    title = form.title.data
    tags = clean_tags(form.tags.data.split(','))

    resource = Resource(current_user.id, title, tags)
    ret = new_resource(resource, tags)
    if ret != RESOURCE_ADD_OK:
        fail(ret)
        return render_template('resource/new.html', form=form)

    save_resource(resource.id, files)

    return redirect(url_for('.index', id=resource.id))

class NewResForm(Form):
    title = TextField(u'标题*', validators=[Required()])
    tags = TextField(u'标签*', validators=[Required()])
