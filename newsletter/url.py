#!/usr/bin/env python
from newsletter import db
from newsletter.redirect import Redirect
from newsletter import EMPTY_GIF_URL
from uuid import uuid4


class LetterUrl(object):
    """
    LetterURL class provides function to get unique url for email campaigns.
    based on the original url or a newsletter-specific url of tracking pixel.

    `__init__` method takes one optional argument
        `base_url` is used to build a full tracking url

    `url` method is used  get unique url for emails

    `letter_id` is mandatory and it should be unique for every email campaign

    an unique url for email
        LetterURL.url(letter_id, email, url)

    if only `letter_id` is specified newsletter-specific url will be created
        LetterURL.url(letter_id)


    `uuid` is optional if it is not specified a new one will be generated based on UUID
    """
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
