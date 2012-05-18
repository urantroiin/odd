# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object("websiteconfig")

#
# Blueprints
#
from odd.views import general

app.register_blueprint(general.mod)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404
