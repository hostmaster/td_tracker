#!/usr/bin/env python

from newsletter import db
from newsletter import EMPTY_GIF_URL

from datetime import datetime


class Redirect(db.Model):
    """
    Redirect class represents a mapping unique ID -> URL
    where ID is a unique identifier which is used as tracking id in url
    Example:
        http://domain.tld/9bc80de6c575407b99891ff15d431259/
        id is 9bc80de6c575407b99891ff15d431259

    URL is destination url where original request should be redirected.
    If URL is not specified it means that. destination url is an url to
    some static assert (an empty gif by default). It could be used to track email
    newsletter opens.

    Other fields are newsletter_id and email.

    ID is a mandatary field. It has to be unique like UUID
    """

    __tablename__ = 'redirects'
    uuid = db.Column(db.String(40), primary_key=True)
    url = db.Column(db.String(256), index=True, unique=False)
    email = db.Column(db.String(128), index=True, unique=False)
    letter_id = db.Column(db.Integer, index=True, unique=False)

    def __init__(self, uuid, email=None, url=EMPTY_GIF_URL, letter_id=None):
        self.uuid = uuid
        self.email = email
        self.url = url
        self.letter_id = letter_id

    def __eq__(self, other):
        return isinstance(other, Redirect) and other.uuid == self.uuid

    def __repr__(self):
        return "< %r : %r >".format(self.uuid, self.url)


class Click(db.Model):
    """
    Click class. It is a 'click' event log record.
    It contents timestamp of the event.
    """

    __tablename__ = 'clicks'
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, index=True)
    uuid = db.Column(db.String(40), db.ForeignKey('redirects.uuid'))

    def __init__(self, uuid):
        self.uuid = uuid
        self.timestamp = datetime.utcnow()

    def __eq__(self, other):
        return isinstance(other, Click) and other.timestamp == self.timestamp and other.uuid == self.uuid

    def __repr__(self):
        return "< %r at %r >".format(self.uuid, self.timestamp())
