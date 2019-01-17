# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 10:16:10 2018

@author: JeremyJone
@content：get method infomation of python objects.
"""

from web.translate import youdao_translate

def getDesc(object, collapse=1, spacing=20, en2chs=False):
    '''
    object：传入想要知道方法的对象
    collapse：显示方式，默认换行显示，设置为0原文显示
    spacing：方法名显示长度，默认20
    en2chs: 英文翻译中文，默认显示英文，设置为True翻译成中文(有道引擎，不甚准确)
    '''
    methodList = [method for method in dir(object) if callable(getattr(object, method))]
    processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
    translate_method = en2chs and (lambda s: youdao_translate(s)) or (lambda s: s)
    print("\n\n\n".join(["%s %s" % (str(method.ljust(spacing)),
                                    translate_method(processFunc(str(getattr(object, method).__doc__))))
                         for method in methodList]))


if __name__ == '__main__':
    import os
    getDesc(os, en2chs=True)

