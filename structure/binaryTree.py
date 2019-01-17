#/usr/bin/env python
# -*- coding: utf-8 -*-
"""
二叉树的实现

@Author: jeremyjone
Create on Thu Jun 21 14:09:56 2018
"""


class Node:
    def __init__(self, item):
        self.item = item
        self._left = None
        self._right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            q = [self.root]

            while True:
                pop_node = q.pop(0)
                if pop_node._left is None:
                    pop_node._left = node
                    return
                elif pop_node._right is None:
                    pop_node._right = node
                    return
                else:
                    q.append(pop_node._left)
                    q.append(pop_node._right)

    # 层次遍历
    def traverse(self):
        if self.root is None:
            return None
        q = [self.root]
        res = [self.root.item]
        while q != []:
            pop_node = q.pop(0)
            if pop_node._left is not None:
                q.append(pop_node._left)
                res.append(pop_node._left.item)

            if pop_node._right is not None:
                q.append(pop_node._right)
                res.append(pop_node._right.item)
        return res

    # 先序遍历
    def preOrder(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.preOrder(root._left)
        right_item = self.preOrder(root._right)
        return result + left_item + right_item

    # 中序遍历
    def inOrder(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.inOrder(root._left)
        right_item = self.inOrder(root._right)
        return left_item + result + right_item

    # 后序遍历
    def postOrder(self, root):
        if root is None:
            return []
        result = [root.item]
        left_item = self.postOrder(root._left)
        right_item = self.postOrder(root._right)
        return left_item + right_item + result



def BFS(tree):
    # 广度优先
    tLst = []
    res = [tree.root.item]
    def traverse(node, p):
        if node._left is not None:
            tLst.append(node._left)
            res.append(node._left.item)
            # print("node._left", node._left.item)
        if node._right is not None:
            tLst.append(node._right)
            res.append(node._right.item)
            # print("node._right", node._right.item)
        if p > (len(tLst) - 2):
            # print("return at ", p)
            return
        else:
            traverse(tLst[p + 1], p + 1)

    tLst.append(tree.root)
    traverse(tree.root, 0)

    return res

def DFS(tree):
    # 深度优先
    tLst = []
    res = []

    tLst.append(tree.root)
    while len(tLst) > 0:
        node = tLst.pop()
        # print(node.item)
        res.append(node.item)
        if node._right is not None:
            tLst.append(node._right)
        if node._left is not None:
            tLst.append(node._left)

    return res


if __name__ == '__main__':
    t = Tree()
    for i in range(10):
        t.add(i)
    print('层序遍历:',t.traverse())
    print('先序遍历:',t.preOrder(t.root))
    print('中序遍历:',t.inOrder(t.root))
    print('后序遍历:',t.postOrder(t.root))
    print('广度优先:', BFS(t))
    print('深度优先:', DFS(t))
