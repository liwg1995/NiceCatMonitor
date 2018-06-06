#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 18/6/6 下午3:08
# @Author  : Wugang Li
# @File    : messages.py
# @Software: PyCharm
# @license : Copyright(C), olei.me
# @Contact : i@olei.me


import json
import ssl
import requests
from conf import config
from tools import logs
import traceback

ssl._create_default_https_context = ssl._create_unverified_context
logs = logs.Writelog('zabbix')

class zabbix():
    def __init__(self):
        self.url = config.zabbix_api
        self.user = config.zabbix_user
        self.password = config.zabbix_password
        self.headers = {"Content-Type": "application/json-rpc"}

    # 获取token
    def get_token(self):
        data = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.user,
                "password": self.password
            },
            "id": 1,
            "auth": None
        }
        value = json.dumps(data)
        try:
            r = requests.post(url=self.url,data=value,headers=self.headers)
            logs.info("获取token:%s" % (r.json()))
            return r.json()['result']
        except:
            logs.error("Error：%s" % (traceback.format_exc()))


    # 获取主机参数
    def host_get(self,hosts):
        token = self.get_token()
        data = {
            "jsonrpc": "2.0",
            "method": "host.get",
            "params": {
                "output": "extend",
                "filter": {
                    "host": [
                        hosts,
                    ]
                }
            },
            "auth": token,
            "id": 1
        }
        value = json.dumps(data)
        try:
            r = requests.post(url=self.url,data=value,headers=self.headers)
            logs.info("获取主机参数:%s" % (r.json()))
            return r.json()['result']
        except:
            logs.error("Error: %s" % (traceback.format_exc()))

    # 获取主机items
    def item_get(self,hostid,key):
        token = self.get_token()
        key_ = key

        data = {
            "jsonrpc": "2.0",
            "method": "item.get",
            "params": {
                "output": "extend",
                "hostids": hostid,
                "search": {
                    "key_": key
                },
                "sortfield": "name"
            },
            "auth": token,
            "id": 1
        }
        value = json.dumps(data)
        try:
            r = requests.post(url=self.url,data=value,headers=self.headers)
            logs.info("获取主机items：%s" % (r.json()))
            return r.json()['result']
        except:
            logs.error("Error: %s" % (traceback.format_exc()))


