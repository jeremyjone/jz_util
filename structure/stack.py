# -*- coding:utf8 -*-
from __future__ import unicode_literals
#/usr/bin/env python
"""
@Author: jeremyjone
Create on Thu Jun 21 13:47:24 2018
"""


class stack():
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1

    def location(self, ele):
        # 返回元素在栈中的位置
        temp = Stack(self.size)
        find = False  # 是否找到
        num = -1  # 找不到返回-1
        while not self.isempty():
            disk = self.pop()
            temp.push(disk)
            if disk == ele:
                find = True  # 找到将find设为true
            if True == find:
                num += 1  # 找到后开始计数

        while not temp.isempty():
            # 将栈内元素归位
            self.push(temp.pop())

        return num

    def push(self, ele):
        # 入栈之前检查栈是否已满
        if self.isfull():
            raise Exception("out of range")
        else:
            self.stack.append(ele)
            self.top = self.top + 1

    def pop(self):
        # 出栈之前检查栈是否为空
        if self.isempty():
            raise Exception("stack is empty")
        else:
            self.top = self.top - 1
            return self.stack.pop()

    def isfull(self):
        return self.top + 1 == self.size

    def isempty(self):
        return self.top == -1

    def getsize(self):
        return self.top + 1

    def __repr__(self):
        if self.isempty():
            return "empty stack"
        node = self.stack
        nlist = ''
        i = 0
        while node:
            if i > self.top:
                break
            nlist += str(node[i]) + ' '
            i += 1
        return nlist

    def __len__(self):
        return self.getsize()



if __name__ == '__main__':
    st = stack(20)
    print(len(st))
    for i in range(15):
        st.push(i)
    print(st)
    a = st.pop()
    print(a)
    print(st)
    print(len(st))
