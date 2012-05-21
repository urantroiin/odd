# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import  url_for, redirect, render_template 
from flaskext.login import login_required, current_user
from flaskext.wtf import Form, TextField, PasswordField, Required

from odd.util.error import *

from odd.biz.user import *

mod = Blueprint('general', __name__)

@mod.route('/')
@mod.route('/login', methods=['GET', 'POST'])
def login():
    '''
    登录
    '''
    form = LoginForm()

    if not form.validate_on_submit():
        return render_template('general/login.html', form=form)

    email = form.email.data
    passwd = form.passwd.data

    user = User(email, passwd)
    ret = login(user)

    if ret != USER_LOGIN_OK:
        fail(ret);
        return redirect(url_for('.login'))
    
    success(ret);
    return redirect(url_for('user.index', id=user.id))

@mod.route('/logout', methods=['POST'])
@login_required
def logout():
    '''
    登出
    '''
    logout()
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
    ret = register(user)

    if ret != USER_REGISTER_OK:
        fail(ret);
        return redirect(url_for('.register'))
    
    success(ret);
    return redirect(url_for('user.index', id=user.id))

# forms
class LoginForm(Form):
    email = TextField(u'邮箱地址', validators=[Required()])
    passwd = PasswordField(u'密码', validators=[Required()])

class RegisterForm(Form):
    email = TextField(u'邮箱地址', validators=[Required()])
    nickname = TextField(u'昵称', validators=[Required()])
    passwd = PasswordField(u'密码', validators=[Required()])
