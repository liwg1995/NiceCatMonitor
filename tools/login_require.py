#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/7 下午3:58
# @Author  : Wugang Li
# @File    : login_require.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from functools import wraps
from flask import session,redirect

def login_message_req(f):
    @wraps(f)
    def check_session(*args,**kwargs):
        if 'xx' not in session:
            return redirect('/login')
        return f(*args,**kwargs)
    return check_session