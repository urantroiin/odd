# -*- coding: utf-8 -*-

from flask import flash

USER_DUPLICATE = u'用户已存在'
USER_NOT_EXIST = u'用户名或密码错误'
USER_LOGIN_OK = u'欢迎光临'
USER_EDIT_OK = u'信息修改成功'
USER_REGISTER_OK = u'注册成功'
USER_LOGOUT_OK = u'注销成功'

QUESTION_ADD_OK = u'问题发布成功'

QUESTION_TAG_ADD_OK = u'tag添加成功'

TAG_FOLLOW_ADD_OK = u'关注成功'

ANSWER_ADD_OK = u'回答成功'

ANSWER_UP_ADD_OK = u'UP成功'
ANSWER_UP_DUPLICATE = u'UP已存在'

COMMENT_ADD_OK = u'评论成功'

TAG_FOLLOW_ADD_OK = u'关注成功'
TAG_FOLLOW_DEL_OK = u'取消关注成功'

def success(error):
    flash(error, 'success')

def fail(error):
    flash(error, 'error')
