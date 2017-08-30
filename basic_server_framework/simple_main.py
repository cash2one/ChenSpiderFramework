#! /usr/bin/env python3
# -*- coding:utf-8 -*-

__author__ = 'Chen Yansu'

'''
代码规范：
1. 统一使用a_b式命名法，避免驼峰命名
2. 长度尽量不要超过79个字符
3. 用协程写
'''



# 系统支持模块
import os
import time
from multiprocessing import Pool
import asyncio

# 爬虫模块
import requests
from lxml import etree
import re

# 数据库支持模块
import redis
import pymysql


# 请求模块

# headers表
headers = [
            {
                # fedora 火狐
                 "User-Agent": "Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:54.0)Gecko/20100101 Firefox/54.0",
                 "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,image/webp,*/*;q=0.8"
            },
            {
                # ubuntu chrome
                 "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/59.0.3071.109 Chrome/59.0.3071.109 Safari/537.36",
                 "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,image/webp,*/*;q=0.8"
            },
            {
                # iPhone safarai
                 "User-Agent": "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",
                 "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,image/webp,*/*;q=0.8"
            },
            {
                # 华为mate8
                 "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; HUAWEI NXT-AL10 Build/HUAWEINXT-AL10) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30",
                 "Accept": "text/html,application/xhtml+xml, application/xml;\q=0.9,image/webp,*/*;q=0.8"
            },
            {   # ubuntu 火狐
                 "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:54.0) Gecko/20100101 Firefox/54.0",
                 "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,image/webp,*/*;q=0.8"
            },
            {
                 "User-Agent": "Mozilla/5.0 (compatible; WOW64; MSIE 10.0; Windows NT 6.2)",
                 "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,image/webp,*/*;q=0.8"
            },

            {
                # win8
                # 360 极速模式
                "User-Agent":"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,image/webp,*/*;q=0.8"
            },

            {
                # win8
                # 360 极速模式
                "User-Agent":"Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; WOW64; Trident/6.0; .NET4.0E; .NET4.0C)",
                "Accept": "text/html,application/xhtml+xml, application/xml;q=0.9,image/webp,*/*;q=0.8"
            },
          ]

def get_request(start_url):
    session = requests.session()
    r = session.get(start_url)
    # rsc 为状态码
    rsc = r.status_code
    # rc 为html正文
    rc = r.content
    return rsc, rc



