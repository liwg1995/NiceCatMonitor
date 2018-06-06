#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/6 下午3:20
# @Author  : Wugang Li
# @File    : logs.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me

import logging
import logging.handlers
import datetime

def Writelog(logName):
    date = datetime.datetime.now().strftime('%Y-%m-%d')
    file = '/tmp/logs-{}'.format(date)
    level = logging.DEBUG

    # 定义日志格式
    format = logging.Formatter('%(asctime)s %(filename)s [line:%(lineno)2d]-%(funcName)s %(levelname)s %(message)s')
    handler = logging.handlers.RotatingFileHandler(filename=file, mode='a', maxBytes=100 * 1024 * 1024, backupCount=100)
    handler.setFormatter(format)

    # 实例化一个日志对象
    logger = logging.getLogger(logName)
    logger.addHandler(handler)
    logger.setLevel(level)
    return logger