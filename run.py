#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/7 下午3:52
# @Author  : Wugang Li
# @File    : run.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from app import app

if __name__ == '__main__':
    app.run(host='127.0.0.1',port=9090,debug=True)