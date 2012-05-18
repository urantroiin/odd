# -*- coding: utf-8 -*-

from flask import Blueprint
from flask import  url_for, redirect, render_template, flash

mod = Blueprint("general", __name__)

@mod.route('/')
def index():
    return render_template("general/index.html")

@mod.route('/wiki')
def wiki():
    return render_template("general/wiki.html")
