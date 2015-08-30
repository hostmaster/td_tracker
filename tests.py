#!/usr/bin/env python

import unittest

from flask import url_for

from newsletter.url import Redirect
from newsletter import EMPTY_GIF_URL

from backend import db
from backend.test_base import BaseTestCase
from uuid import uuid4


class UrlRedirectTests(BaseTestCase):

    def test_request_to_index(self):
        response = self.client.get(url_for('index'))
        self.assert_200(response)

    def test_url_redirected_by_uuid(self):
        _uuid = uuid4().hex
        _url = 'http://ya.ru'
        url = Redirect(uuid=_uuid, url=_url)
        db.session.add(url)
        db.session.commit()

        response = self.client.get(url_for('redirect_url', uuid=_uuid))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, _url)

        response = self.client.get(url_for('redirect_url', uuid=_uuid))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, _url)

    def test_newsletter_url(self):
        _uuid = uuid4().hex
        _letter = '11'
        url = Redirect(uuid=_uuid, letter_id=_letter)

        db.session.add(url)
        db.session.commit()

        response = self.client.get(url_for('redirect_url', uuid=_uuid))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, EMPTY_GIF_URL)

    def test_url_notfound(self):
        response = self.client.get(url_for('redirect_url', uuid='xxx'))
        self.assertRedirects(response, url_for('notfound'))

if __name__ == '__main__':
    unittest.main()
