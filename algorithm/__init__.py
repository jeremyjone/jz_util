#!/usr/bin/env python
# -*- coding:utf8 -*-
'''
排序方法

@Author: jeremyjone
create on Thu Jun 21 11:58:42 2018
'''




def maxmin(L, start=None, end=None):
    if not start:
        start = 0

    if not end:
        end = len(L) - 1

    if end - start <= 1:
        return (max(L[start], L[end]), min(L[start], L[end]))
    else:
        max1, min1 = maxmin(L, start, (start + end) // 2)
        max2, min2 = maxmin(L, (start + end) // 2 + 1, end)
        return (max(max1, max2), min(min1, min2))