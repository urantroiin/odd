# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flaskext.login import LoginManager

app = Flask(__name__)
app.config.from_object("websiteconfig")

#
# Blueprints
#
from odd.views import general
from odd.views import user
from odd.views import question
from odd.views import answer
from odd.views import tag
from odd.views import search
from odd.views import follow
from odd.views import remind

app.register_blueprint(general.mod)
app.register_blueprint(user.mod)
app.register_blueprint(question.mod)
app.register_blueprint(answer.mod)
app.register_blueprint(tag.mod)
app.register_blueprint(search.mod)
app.register_blueprint(follow.mod)
app.register_blueprint(remind.mod)

#
# Login
#
from odd.biz.user import get_user_by_id

login_manager = LoginManager()
login_manager.setup_app(app)
login_manager.login_view = "general.login"
login_manager.login_message = u"这个页面需要登录后才能访问"

@login_manager.user_loader
def load_user(user_id):
    return get_user_by_id(user_id)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
