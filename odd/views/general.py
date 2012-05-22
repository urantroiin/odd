# -*- coding: utf-8 -*-

from flask import Blueprint, url_for, redirect, render_template, abort
from flaskext.login import login_required, current_user
from flaskext.wtf import Form, TextField, PasswordField, BooleanField, Required, Email, EqualTo, Regexp, ValidationError

from odd.utils.error import *

from odd.biz.user import *

mod = Blueprint('general', __name__)

@mod.route('/')
def index():
    '''
    首页
    '''
    form = LoginForm()
    return render_template('general/login.html', form=form)


@mod.route('/login', methods=['GET','POST'])
def login():
    '''
    登录
    '''
    form = LoginForm()

    if not form.validate_on_submit():
        return render_template('general/login.html', form=form)

    email = form.email.data
    passwd = form.passwd.data
    auto = form.auto.data

    user = User(email, passwd)
    ret = user_login(user, auto)

    if ret != USER_LOGIN_OK:
        fail(ret);
        return render_template('general/login.html', form=form)
    
    success(ret);
    return redirect(url_for('user.index', nickname=user.nickname))

@mod.route('/logout', methods=['GET','POST'])
@login_required
def logout():
    '''
    登出
    '''
    user_logout()
    return redirect(url_for('.index'))

@mod.route('/register', methods=['GET', 'POST'])
def register():
    '''
    注册
    '''
    form = RegisterForm()

    if not form.validate_on_submit():
        return render_template('general/register.html', form=form)

    email = form.email.data
    nickname = form.nickname.data
    passwd = form.passwd.data

    user = User(email, passwd, nickname)
    ret = register_user(user)

    if ret != USER_REGISTER_OK:
        fail(ret);
        return render_template('general/register.html', form=form)
    
    success(ret);
    return redirect(url_for('user.index', nickname=user.nickname))

# forms
def BeTrue(msg):
        def _BeTrue(form, field):
            if not field.data:
                raise ValidationError(msg)
        return _BeTrue

class LoginForm(Form):
    email = TextField(u'邮箱地址', validators=[Required(), Email()])
    passwd = PasswordField(u'密码', validators=[Required(),Regexp('[\w\d-]{5,20}')])
    auto = BooleanField(u'自动登录', default=True)

class RegisterForm(Form):
    email = TextField(u'邮箱地址*', validators=[Required(), Email()])
    nickname = TextField(u'昵称*', validators=[Required(),Regexp('[\w\d-]{2,20}')])
    passwd = PasswordField(u'密码*', validators=[Required(),Regexp('[\w\d-]{5,20}')])
    confirm = PasswordField(u'确认密码*', validators=[Required(), EqualTo('passwd', message=u'密码不一致')])
    agree = BooleanField(u'我已经认真阅读并同意', default=True, validators=[BeTrue(u'同意此协议才能注册')])
