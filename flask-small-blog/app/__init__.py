#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan

"""
import os
from flask import Flask
from app.forms import LoginForm
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from config import basedir

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir,'tmp'))

from app import views,models