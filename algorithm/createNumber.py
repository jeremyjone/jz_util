#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
一些特殊数字的生成器包，像素数、斐波那契数等

@Author: jeremyjone
create on Thu Jun 21 14:17:16
'''


class Prime(object):
    # 生成素数
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        # 设定迭代的当前位置为开始值
        self.current = start

    def isprime(self, num):
        for x in range(2, num):
            if num % x == 0:
                return False
        return True

    def __next__(self):
        # 判断当前走过的值是否到达重点，如果没有，继续
        while self.current < self.stop:
            v = self.current  # 保存当前值
            self.current += 1   # 让迭代位置向后走一步
            if self.isprime(v):
                return v
        # self.current < self.stop 不成立时
        # 抛出StopIteration异常
        raise StopIteration

    def __iter__(self):
        return self

    def next(self):
        '''python2 需要添加此方法'''
        return self.__next__()



class Fabonacci(object):
    # 生成斐波那契数
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        a, b, m = 0, 1, 0
        while m < self.n:
            a, b, m = a + b, a, m + 1
            yield a

    def __next__(self):
        return self

    def next(self):
        '''python2需要添加此方法'''
        return self.__next__()



if __name__ == '__main__':
    # 测试语句
    for x in Prime(10, 50):
        print(x)
    for i in Fabonacci(20):
        print(i)