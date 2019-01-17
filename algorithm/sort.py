#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
排序方法

@Author: jeremyjone
create on Thu Jun 21 11:58:42 2018
'''
from __future__ import unicode_literals


class JSort(object):
    '''
    传入要排序的数据列表，返回排序结果
    包含多种排序方法

    使用方法：
    s = mysort(data)  --->  s.排序函数()  --->  返回排序后结果
    '''

    def __init__(self, data):
        self.data = data

    def quickSort(self):
        # 排序函数，由两个游标分别从两端开始遍历
        # 左端数据要比基数小，所以判断条件是遇到
        # 比基数大的就要停下。
        # 右端的情况与左端相反。
        #
        # 注意：程序一定要先从右端开始遍历，因为
        #       两端遍历最终停下的条件肯定是相遇
        #       的时候，如果左端先移动，则最后停
        #       下时的数值肯定比基数大，若将这个
        #       数字与基数交换，则基数左边的数字
        #       就不是全部比基数小了，程序运行就
        #       不正确了。
        # 快排的时间复杂度最佳情况是O(nlogn)，最差情况是O(n^2)
        def _sort(left, right):
            if(left > right):
                return
            temp = self.data[left]
            i = left
            j = right
            while i != j:
                while(self.data[j] >= temp and i < j):
                    j -= 1
                while(self.data[i] <= temp and i < j):
                    i += 1
                if i < j:
                    self.data[i], self.data[j] = self.data[j], self.data[i]
            self.data[left], self.data[i] = self.data[i], temp
            _sort(left, i-1)
            _sort(i+1, right)

        _sort(0, len(self.data)-1)
        return self.data

    def bubbleSort(self):
        # 冒泡排序，列表中每相邻两个如果顺序不是我们预期的大小排列，则交换。
        #　时间复杂度O(n^2)
        # 定一个最高位
        high = len(self.data)-1
        for j in range(high, 0, -1):
            # 交换的标志，如果提前排好序可在完整遍历前结束
            exchange = False
            for i in range(0, j):
                # 如果比下一位大
                if self.data[i] > self.data[i+1]:
                    # 交换位置
                    self.data[i], self.data[i+1] = self.data[i+1], self.data[i]
                    # 设置交换标志
                    exchange = True
            if exchange == False:
                return self.data

    def choiceSort(self):
        # 选择排序，一趟遍历选择最小的数放在第一位，再进行下一次遍历直到最后一个元素。
        # 复杂度为O(n^2)
        for i in range(0, len(self.data)):
            min_loc = i
            for j in range(i+1, len(self.data)):
                # 最小值遍历比较
                if self.data[min_loc] > self.data[j]:
                    min_loc = j
            self.data[i], self.data[min_loc] = self.data[min_loc], self.data[i]
        return self.data

    def insertSort(self):
        # 插入排序，将列表分为有序区和无序区，最开始的有序区只有一个元素,
        # 每次从无序区选择一个元素按大小插到有序区中。
        # 复杂度为O(n^2)
        for i in range(1, len(self.data)):
            temp = self.data[i]
            # 从有序区最大值开始遍历
            for j in range(i-1, -1, -1):
                # 如果待插入值小于有序区的值
                if self.data[j] > temp:
                    # 向后挪一位
                    self.data[j+1] = self.data[j]
                    # 将temp放进去
                    self.data[j] = temp
        return self.data

    def heapSort(self):
        # 堆排序，过程如下：
        # 建立堆
        # 得到堆顶元素，为最值
        # 去掉堆顶，将最后一个元素放到堆顶，进行再一次堆排序（迭代）
        # 第二次的堆顶为第二最值
        # 重复上两条直到堆为空
        def sift(low, high, data):
            # low为父节点，high为最后的节点编号
            i = low
            # 子节点位置
            j = 2 * i + 1
            # 存放临时变量
            temp = data[i]
            # 遍历子节点到最后一个
            while j <= high:
                # 如果第二子节点大于第一子节点
                if j < high and data[j] < data[j + 1]:
                    j += 1
                # 如果父节点小于子节点的值
                if temp < data[j]:
                    # 父子交换位置
                    data[i] = data[j]
                    # 进行下一次编号
                    i = j
                    j = 2 * i + 1
                else:
                    # 遍历完毕退出
                    break
            # 归还临时变量
            data[i] = temp

        n = len(self.data)
        # 从最后一个父节点开始
        for i in range(n // 2 - 1, -1, -1):
            # 完成堆排序
            sift(i, n-1, self.data)
        # 开始排出数据
        for i in range(n - 1, -1, -1):
            # 首尾交换
            self.data[0], self.data[i] = self.data[i], self.data[0]
            # 进行新一轮堆排序
            sift(0, i - 1, self.data)
        return self.data

    def mergeSort(self):
        # 归并排序：假设列表中可以被分成两个有序的子列表，
        # 如何将这两个子列表合成为一个有序的列表成为归并。
        def _MergeSort(lists):
            if len(lists) <= 1:
                return lists
            num = int(len(lists) / 2)
            left = _MergeSort(lists[:num])
            right = _MergeSort(lists[num:])
            return _Merge(left, right)

        def _Merge(left, right):
            r, l = 0, 0
            result = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
            result += right[r:]
            result += left[l:]
            return result
        return _MergeSort(self.data)


if __name__ == '__main__':
    data = [3, 1, 5, 7, 8, 6, 2, 0, 4, 9]
    # data = []

    qs = JSort(data)
    print("quick_sort:", qs.quickSort())
    print("bubble_sort:", qs.bubbleSort())
    print("choice_sort:", qs.choiceSort())
    print("insert_sort:", qs.insertSort())
    print("heap_sort:", qs.heapSort())
    print("merge_sort:", qs.mergeSort())
