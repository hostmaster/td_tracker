#!/usr/bin/env python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

backend = Flask(__name__)
backend.config.from_object('config.BaseConfiguration')
db = SQLAlchemy(backend)

from backend import views, models
