# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort, request, jsonify
from flask.ext.login import login_required, current_user

from odd.utils.error import *

from odd.biz.follow import *

from re import match

mod = Blueprint('follow', __name__, url_prefix='/follow')

@mod.route('/')
@login_required
def index():
    return ''


@mod.route('/tag/follow', methods=['POST'])
@login_required
def tag_follow():
    tag = request.form.getlist('tag')
    if not tag:
        return jsonify(errno='FAIL')
    
    tag_follow = Tag_Follow(current_user.id, tag[0])
    ret = new_tag_follow(tag_follow)
    if ret != TAG_FOLLOW_ADD_OK:
        return jsonify(errno='FAIL')

    return jsonify(errno='SUCCESS')

@mod.route('/tag/unfollow', methods=['POST'])
@login_required
def tag_unfollow():
    tag = request.form.getlist('tag')
    if not tag:
        return jsonify(errno='FAIL')
    
    tag_follow = Tag_Follow(current_user.id, tag[0])
    ret = del_tag_follow(tag_follow)
    if ret != TAG_FOLLOW_DEL_OK:
        return jsonify(errno='FAIL')

    return jsonify(errno='SUCCESS')
