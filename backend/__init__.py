#!/usr/bin/env python
from flask import Flask
from newsletter import db

backend = Flask(__name__)
backend.config.from_object('config.BaseConfiguration')
# db = SQLAlchemy(backend)
db.init_app(backend)

from backend import views, models
