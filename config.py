#!/usr/bin/env python
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfiguration(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data/backend.db')


class TestConfiguration(BaseConfiguration):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
