from flask import render_template, redirect, request, url_for, flash, make_response
from flask.ext.login import login_required, logout_user, current_user
from . import main
from .. import db

@main.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')
