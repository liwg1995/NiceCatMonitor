#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/7 下午3:41
# @Author  : Wugang Li
# @File    : views.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from app import app
from flask import Flask, session,redirect,render_template


@app.route("/login/",methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/',methods=['GET','POST'])
def index():
    return redirect('/dashboard')

@app.route('user/info',methods=['GET','POST'])
def user_info():
    return render_template('user_info.html')