#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/7 下午6:04
# @Author  : Wugang Li
# @File    : forms.py.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField
from wtforms.validators import DataRequired,ValidationError

class Login(FlaskForm):
    admin = StringField(
        label="管理员账号",
        validators=[
            DataRequired("账号不能为空!")
        ],
        description="账号",
        render_kw={
            "class":"xxx",
            "placeholder":"请输入管理员账号",
            "required":"required"
        }
    )
    pwd = PasswordField(
        label="密码",
        validators=[
            DataRequired("密码不能为空!")
        ],
        description="账号",
        render_kw={
            "class":"xxx",
            "palceholder":"请输入管理密码",
            "required":"required"
        }
    )
    submit = SubmitField(
        "登录",
        render_kw={
            "class":"xxx"
        }
    )