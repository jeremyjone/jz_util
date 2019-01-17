# !/usr/bin/env python
# -*- coding:utf-8 -*-
"""
列表去重方法
"""
__author__ = "jeremyjone"
__datetime__ = "2019/1/2 11:56"
__all__ = ["__version__", ]
__version__ = "1.0.0"


def fn1(lst):
    _l = list(set(lst))
    # 让列表重新按照原来lst的下标进行排序,保持剩余元素和原来顺序一致
    _l.sort(key=lst.index)
    return _l


def fn2(lst):
    new_lst = []
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst


def fn3(lst):
    for i in lst:
        # 循环判断每一个元素在lst里的个数,如果大于1,删除
        # 需要注意的是,这里不能用if,应该使用while
        # 因为使用lst.pop(i)之后,lst本身的下标会改变,需要使用while进行更新
        while lst.count(i) > 1:
            lst.pop(i)
    return lst


def fn4(lst):
    myDict = {}
    for i in lst:
        myDict[i] = 0
    return list(myDict.keys())


if __name__ == '__main__':
    lst = [1, 1, 1, 9, 2, 3, 4, 5, 5, 6, 7, 8, 9, 0]
    print("fn1>>", fn1(lst))  # ('fn1>>', [1, 9, 2, 3, 4, 5, 6, 7, 8, 0])
    print("fn2>>", fn2(lst))  # ('fn2>>', [1, 9, 2, 3, 4, 5, 6, 7, 8, 0])
    print("fn3>>", fn3(lst))  # ('fn3>>', [1, 9, 2, 3, 4, 5, 6, 7, 0])
    print("fn4>>", fn4(lst))  # ('fn4>>', [0, 1, 2, 3, 4, 5, 6, 7, 9])



