#!/usr/bin/env python
from flask_testing import TestCase
from newsletter import db
from backend import backend


class BaseTestCase(TestCase):
    """ A base test case for backend redirector. """

    def create_app(self):
        backend.config.from_object('config.TestConfiguration')
        return backend

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
