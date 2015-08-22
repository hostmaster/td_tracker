#!/usr/bin/env python
from backend import db


class Newsletter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subj = db.Column(db.String(256), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.subj)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), index=True, unique=True)

    def __repr__(self):
        return '<User %r>' % (self.email)


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String(40), index=True, unique=True)
    url = db.Column(db.String(256), index=False, unique=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    newsletter_id = db.Column(db.Integer, db.ForeignKey('newsletter.id'))

    def __repr__(self):
        return '<UUID %r URL %r>'.format(self.uuid, self.url)
