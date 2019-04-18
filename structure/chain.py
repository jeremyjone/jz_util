# -*- coding:utf8 -*-
#/usr/bin/env python
"""
@Author: jeremyjone
Create on Thu Jun 21 10:52:51
"""
from __future__ import unicode_literals


class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self._next = next

    def __repr__(self):
        return str(self.data)


class ChainTable(object):
    def __init__(self):
        self.head = None
        self.length = 0

    def isEmpty(self):
        # 判断链表是否为空
        return self.length == 0

    def append(self, dataOrNode):
        # 向链表中追加数据或节点
        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if not self.head:
            self.head = item
            self.length += 1

        else:
            node = self.head
            while node._next:
                node = node._next
            node._next = item
            self.length += 1

    def delete(self, index):
        # 根据接收的Index删除相应节点
        if self.isEmpty():
            print("this chain table is empty.")
            return

        if index < 0 or index >= self.length:
            print('error: out of index')
            return
        # 要注意删除第一个节点的情况
        if index == 0:
            self.head = self.head._next
            self.length -= 1
            return

        # prev为保存前导节点
        # node为保存当前节点
        # 当j与index相等时就相当于找到要删除的节点
        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            prev._next = node._next
            # 删除一个节点之后记得要把链表长度减一
            self.length -= 1

    def insert(self, index, dataOrNode):
        # 在给出的Index位置插入数据或节点，其后面节点依次向后顺延
        if self.isEmpty():
            print("this chain tabale is empty")
            return

        if index < 0 or index >= self.length:
            print("error: out of index")
            return

        item = None
        if isinstance(dataOrNode, Node):
            item = dataOrNode
        else:
            item = Node(dataOrNode)

        if index == 0:
            item._next = self.head
            self.head = item
            self.length += 1
            return

        j = 0
        node = self.head
        prev = self.head
        while node._next and j < index:
            prev = node
            node = node._next
            j += 1

        if j == index:
            item._next = node
            prev._next = item
            self.length += 1

    def update(self, index, data):
        # 更新Index位置的节点数据
        if self.isEmpty() or index < 0 or index >= self.length:
            print('error: out of index')
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        if j == index:
            node.data = data

    def getItem(self, index):
        # 获取Index节点的数据对象
        if self.isEmpty() or index < 0 or index >= self.length:
            print("error: out of index")
            return
        j = 0
        node = self.head
        while node._next and j < index:
            node = node._next
            j += 1

        return node.data

    def getIndex(self, data):
        # 获取数据值当前对应的Index列表
        j = 0
        if self.isEmpty():
            print("this chain table is empty")
            return
        node = self.head
        res = []
        while node:
            if node.data == data:
                res.append(j)
            node = node._next
            j += 1

        if res:
            return res
        else:
            print("%s not found" % str(data))
            return

    def clear(self):
        # 清空链表
        self.head = None
        self.length = 0

    def __repr__(self):
        if self.isEmpty():
            return "empty chain table"
        node = self.head
        nlist = ''
        while node:
            nlist += str(node.data) + ' '
            node = node._next
        return nlist

    def __getitem__(self, ind):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print("error: out of index")
            return
        return self.getItem(ind)

    def __setitem__(self, ind, val):
        if self.isEmpty() or ind < 0 or ind >= self.length:
            print("error: out of index")
            return
        self.update(ind, val)

    def __len__(self):
        return self.length

    def __iter__(self):
        # 可迭代
        node = self.head
        while True:
            yield node.data
            if not node._next:
                raise StopIteration
            node = node._next


if __name__ == '__main__':
    ct = ChainTable()
    for i in range(10):
        ct.append(i)
    print(ct)
    import time
    for i in ct:
        time.sleep(0.5)
        print(i)
