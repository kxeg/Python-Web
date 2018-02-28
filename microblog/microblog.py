#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan

"""
from app import app,db
from app.models import User,Post

@app.shell_context_processor #将该函数注册为shell上下文函数
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}