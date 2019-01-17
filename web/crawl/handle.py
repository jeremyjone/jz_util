# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
一些爬虫常用函数
"""
__author__ = "jeremyjone"
__datetime__ = "2019/1/2 12:22"
__all__ = ["__version__", "getStatusCode", ]
__version__ = "1.0.0"
import requests


def getStatusCode():
    headers = {"User-Agent": "jeremyjone"}
    response = requests.get("http://www.baidu.com", headers=headers)
    response.encoding = "utf-8"
    return response.status_code


if __name__ == '__main__':
    print(getStatusCode())