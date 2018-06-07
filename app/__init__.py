#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/6 下午5:18
# @Author  : Wugang Li
# @File    : __init__.py.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/zabbix'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '22e082448b7349eaacb8d30d375af71f'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/zabbix'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = '22e082448b7349eaacb8d30d375af71f'

app.debug = True
db = SQLAlchemy(app)