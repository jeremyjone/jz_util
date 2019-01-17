# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
command information
"""
__author__ = "jeremyjone"
__datetime__ = "2018/12/29 17:47"
__all__ = ["__version__", "getHostIP", "getHostUser"]
__version__ = "1.0.0"


def getHostIP():
    '''get_host_ip()  # 获取本机的IP'''
    import socket
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def getHostUser():
    '''get_user()  # 获取本机登录用户名'''
    import getpass
    return getpass.getuser()