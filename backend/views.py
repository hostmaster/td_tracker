#!/usr/bin/env python
from flask import render_template, redirect, url_for

from backend import backend
from newsletter import db
from newsletter.redirect import Redirect, Click


@backend.route('/<uuid>')
def redirect_url(uuid):
    url = Redirect.query.filter_by(uuid=uuid).first()
    if not url:
        url = url_for('notfound')
    else:
        click = Click(uuid)
        db.session.add(click)
        db.session.commit()
    return redirect(url)


@backend.route('/notfound')
def notfound():
    return render_template('notfound.html')


@backend.route('/')
@backend.route('/index')
def index():
    return render_template('index.html')
