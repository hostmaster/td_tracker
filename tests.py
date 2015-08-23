#!/usr/bin/env python

import unittest

from flask import url_for

from backend import db
from backend.test_base import BaseTestCase
from backend.models import Url


class UrlRedirectTests(BaseTestCase):

    def test_request_to_index(self):
        response = self.client.get(url_for('index'))
        self.assert_200(response)

    def test_url_redirected_by_uuid(self):
        _uuid = '5805614c497c11e58cf83c15c2c43f78'
        _url = 'http://ya.ru'
        url = Url(uuid=_uuid, url=_url)
        db.session.add(url)
        db.session.commit()

        response = self.client.get(url_for('redirect_url', uuid=_uuid))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, _url)

    def test_url_redirected_uuid_generated(self):
        _url = 'http://goo.gl'
        url = Url(url=_url)
        _uuid = url.uuid

        db.session.add(url)
        db.session.commit()

        response = self.client.get(url_for('redirect_url', uuid=_uuid))

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.location, _url)

    def test_url_notfound(self):
        _uuid = '5805614c497c11e58cf83c15c2c43f78'
        _url = 'http://ya.ru'
        url = Url(uuid=_uuid, url=_url)
        db.session.add(url)
        db.session.commit()

        response = self.client.get(url_for('redirect_url', uuid='xxx'))

        self.assertRedirects(response, url_for('notfound'))

if __name__ == '__main__':
    unittest.main()
