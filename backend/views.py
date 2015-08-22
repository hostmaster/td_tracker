#!/usr/bin/env python
from flask import render_template, redirect, url_for
from backend import backend
from .models import Url


@backend.route('/u/<uuid>/')
def redirect_url(uuid):
    url = Url.query.filter_by(uuid=uuid).first()
    if not url:
        url = url_for('notfound')
    return redirect(url)


@backend.route('/notfound')
def notfound():
    return render_template('notfound.html')


@backend.route('/')
@backend.route('/index')
def index():
    return render_template('index.html')
