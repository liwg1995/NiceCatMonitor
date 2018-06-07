#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/7 下午3:41
# @Author  : Wugang Li
# @File    : views.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from app import app
from flask import Flask, session, redirect, render_template, flash, url_for, request
from app.forms import LoginForm
from app.models import Users
from tools import login_require


@login_require.login_message_req
@app.route("/login/", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        admin = Users.query.filter_by(name=data['admin']).first()
        if not admin.check_pwd(data['pwd']):
            flash("密码错误")
            return redirect("/login/")
        session['admin'] = data['admin']
        return redirect(request.args.get("next") or url_for("/"))
    return render_template('login.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def index():
    return redirect('/dashboard')


@login_require.login_message_req
@app.route('user/info', methods=['GET', 'POST'])
def user_info():
    return render_template('user_info.html')
