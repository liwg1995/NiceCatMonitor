#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/6 下午5:19
# @Author  : Wugang Li
# @File    : models.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

import pymysql
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from app import db


class Users(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    name_cn = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(80), nullable=True)
    mobile = db.Column(db.String(11), nullable=False)
    role = db.Column(db.String(10), nullable=False)
    status = db.Column(db.SmallInteger, nullable=True)
    create_time = db.Column(db.DateTime, index=True, default=datetime.now())
    last_time = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return "<User:%r>" % self.name


class Servers_Info(db.Model):
    __tablename__ = "servers_Info"
    sid = db.Column(db.Integer, primary_key=True)
    # sid = db.Column(db.Integer, db.ForeignKey('servers_Status.sid'), primary_key=True)
    machine_room = db.Column(db.String(30), nullable=True)
    cabinet = db.Column(db.Integer, nullable=True)
    sn = db.Column(db.String(100), unique=True, nullable=False)
    server_type = db.Column(db.String(64), nullable=False)
    configuration = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return "<Machine:%r>" % self.machine_room


class Servers_Status(db.Model):
    __tablename__ = 'servers_Status'
    sid = db.Column(db.Integer, primary_key=True)
    # sid = db.relationship('Servers_Info', backref='servers_Status')
    server_name = db.Column(db.String(50), nullable=True)
    status = db.Column(db.Integer, nullable=True)
    ip = db.Column(db.String(255), nullable=True)
    services = db.Column(db.String(64), nullable=True)

    def __repr__(self):
        return "<Server_name:%r>" % self.server_name


if __name__ == '__main__':
    db.create_all()
