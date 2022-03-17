# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.11 11:27
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2,2]
示例 2:

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[4,9]
 

说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现次数的最小值一致。
我们可以不考虑输出结果的顺序。
进阶：

如果给定的数组已经排好序呢？你将如何优化你的算法？
如果 nums1 的大小比 nums2 小很多，哪种方法更优？
如果 nums2 的元素存储在磁盘上，内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2y0c2/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def del_item(l: List, value: int):
    index = l.index(value)
    del l[index]


def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    # 遍历较少的数组，如果在另一个数组里找到了就从一个数组删掉一个值，并将该值放入结果集，直到遍历完成
    # result_list = []
    # n1 = len(nums1)
    # n2 = len(nums2)
    #
    # if n1 > n2:
    #     nums1, nums2 = nums2, nums1
    #     n1, n2 = n2, n1
    #
    # for i in range(n1):
    #     if nums1[i] in nums2:
    #         del_item(nums2, nums1[i])
    #         result_list.append(nums1[i])
    #
    # return result_list

    # 排序 + 双指针
    result_list = []
    n1 = len(nums1)
    n2 = len(nums2)
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    while i < n1 and j < n2:
        if nums1[i] == nums2[j]:
            result_list.append(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return result_list


if __name__ == '__main__':
    value_min = 1
    value_max = 9
    len_min = 3
    len_max = 9
    nums1 = [random.randint(value_min, value_max) for i in range(random.randint(len_min, len_max))]
    nums2 = [random.randint(value_min, value_max) for i in range(random.randint(len_min, len_max))]

    pprint(nums1)
    pprint(nums2)
    pprint(intersect(nums1, nums2))

    pass
