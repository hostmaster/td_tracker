#!/usr/bin/env python
from newsletter import db
from newsletter.redirect import Redirect
from newsletter import EMPTY_GIF_URL
from uuid import uuid4
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError


# http://skien.cc/blog/2014/02/06/sqlalchemy-and-race-conditions-follow-up/
def get_one_or_create(session,
                      model,
                      create_method='',
                      create_method_kwargs=None,
                      **kwargs):
    try:
        return session.query(model).filter_by(**kwargs).one(), True
    except NoResultFound:
        kwargs.update(create_method_kwargs or {})
        created = getattr(model, create_method, model)(**kwargs)
        try:
            session.add(created)
            session.flush()
            return created, False
        except IntegrityError:
            session.rollback()
            return session.query(model).filter_by(**kwargs).one(), True


class LetterUrl(object):
    def __init__(self, base_url="http://localhost/"):
        if not base_url.endswith('/'):
            base_url += '/'
        if not base_url.startswith('http'):
            base_url = 'http://' + base_url
        self.base_url = base_url

    def __build_url(self, uuid):
        return self.base_url + uuid

    def url(self, letter_id, email=None, url=EMPTY_GIF_URL, uuid=None):
        if not uuid:
            uuid = uuid4().hex
        redir = Redirect(uuid=uuid, email=email, url=url, letter_id=letter_id)
        db.session.add(redir)
        db.session.commit()
        return (self.__build_url(redir.uuid), uuid)
