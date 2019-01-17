# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:36:31 2018

@author: JeremyJone
@content：language translate.
"""

import random
import json
from crawl import UAPool
from urllib import request, parse


UA = UAPool.get_user_agent_pc()


def youdao_translate(translate_text):
    '''
    English translate to Chinese.
    '''
    youdaoURL = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=https://www.baidu.com/link'
    headers = {"User-Agent": UA,
               "X-Requested-With": "XMLHttpRequest",  # Ajax声明
               "Accept": "application/json, text/javascript, */*; q=0.01",  # 接收数据类型声明，json
               "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
               }
    formdata = {"i": translate_text,
                "from": "AUTO",
                "to": "AUTO",
                "smartresult": "dict",
                "client": "fanyideskweb",
                "salt": "1527149978671",
                "sign": "e78a55589733e3919842551ea5fd0bf6",
                "doctype": "json",
                "version": "2.1",
                "keyfrom": "fanyi.web",
                "action": "FY_BY_REALTIME",
                "typoResult": "false", }

    # 做urlencode，参数要求使用bytes类型
    data = parse.urlencode(formdata).encode("utf-8")
    req = request.Request(youdaoURL, data, headers=headers, method="POST")
    response = request.urlopen(req)
    info = response.read().decode("utf-8")
    info = json.loads(info)
    res = info["translateResult"][0][0]["tgt"]
    return res


if __name__ == '__main__':
    print(youdao_translate("English translate to Chinese."))