#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
# @Author  : xuan

"""
from flask import render_template,flash,redirect,url_for,request
from app import app
from app.forms import LoginForm
from app.models import User
from flask_login import current_user,login_user,logout_user
from werkzeug.urls import url_parse

@app.route('/')
@app.route('/index')
def index():
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title="Home Page", posts=posts)

@app.route('/login',methods=['GET','POST'])
def login():
    if current_user.id_authenticated: #如果用户拥有有效验证的话为True
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit(): #浏览器发送get返回false
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user,remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title="Sign In", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))