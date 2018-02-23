#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan

"""
from app import db

class User(db.Model):
    id = db.Column(db.Integer,permary_key = True)
    nickname = db.Column(db.String(64), index= True, unique = True)
    email = db.Column(db.String(120), index = True, unique = True)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    @property
    def id_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return str(self.id)
        except NameError:
            return unicode(self.id)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

class Post(db.Model):
    id  = db.Column(db.Interger, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>'% (self.body)