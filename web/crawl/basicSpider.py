# -*- coding: utf-8 -*-
"""
简单的爬虫，可以爬取网页源码。
"""
__author__ = "jeremyjone"
__datetime__ = "2017/5/28 17:41"
__all__ = ["__version__", "downloadHTML", ]
__version__ = "1.0.0"
import os
import sys
import random
import time

if sys.version_info >= (3,):
    import urllib
    from urllib.request import urlopen, ProxyHandler, build_opener, install_opener
else:
    import urllib2 as urllib
    from urllib2 import urlopen, ProxyHandler, build_opener, install_opener

from file.jlog import JLog



logger = JLog(os.path.expanduser(os.path.join('~', 'basicProxy.log')))


PROXY_RANGE_MIN = 1
PROXY_RANGE_MAX = 10
PROXY_RANGE = 2


def downloadHTML(url, headers=[], proxy={}, num_retries=10,
                 timeout=10, decodeInfo="utf-8"):
    """
    爬虫的GET请求，考虑了UA等http、request、head部分的设置；
    支持代理服务器的信息处理；
    返回的状态码不是200何如处理；
    支持超时的处理；
    支持网页编码的问题
    """
    # 返回值，初始值为None
    html = None
    # 递归出口
    if num_retries <= 0:
        return html

    # 一般情况下，使用UA池和proxy池相结合方式来访问某个页面，会更加不容易被反爬
    # 动态的调整代理服务器的使用策略，有概率不使用代理服务器
    if random.randint(PROXY_RANGE_MIN, PROXY_RANGE_MAX) >= PROXY_RANGE:
        logger.info("No Proxy")
        proxy = None

    proxy_handler = ProxyHandler(proxy)
    # 替换handler，实现处理proxy
    opener = build_opener(proxy_handler)
    # 设置访问的headers
    opener.addheaders = headers
    # 把opener装载进urllib库中，准备使用
    install_opener(opener)

    try:
        response = urlopen(url)
        html = response.read().decode(decodeInfo)
    except UnicodeDecodeError:
        # 编码错误
        logger.error("UnicodeDecodeError")
    except urllib.error.URLError or urllib.error.HTTPError as e:
        # urllib包错误问题，包含了多种可能，需要分别记录日志
        logger.error("urllib error")
        if hasattr(e, "code") and 400 <= e.code < 500:
            # 客户端问题
            logger.error("Client Error")
        elif hasattr(e, "code") and 500 <= e.code < 600:
            # 服务器端问题
            logger.error("Server Error")
            # 服务器出问题，重复尝试
            html = downloadHTML(
                url, headers, proxy, timeout, decodeInfo, num_retries - 1)
            # 出现问题，休息一段时间再次尝试
            time.sleep(PROXY_RANGE)
    except Exception:
        logger.error("Download Error")

    return html


if __name__ == "__main__":
    url = "http://www.baidu.com"
    headers = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36")]
    proxy = {"http": "183.129.243.84:9000"}

    print(downloadHTML(url, headers, proxy))


