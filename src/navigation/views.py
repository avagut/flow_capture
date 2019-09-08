from . import bl_nav
from flask import render_template

@bl_nav.route('/')
def hello():
    return render_template('index.html')