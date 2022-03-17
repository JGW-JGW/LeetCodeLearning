# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.11 09:05
# Author  : Seto.Kaiba
from pprint import pprint
import random

"""
给定一个整数数组，判断是否存在重复元素。

如果存在一值在数组中出现至少两次，函数返回 true 。如果数组中每个元素都不相同，则返回 false 。

 

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x248f5/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def containsDuplicate(nums: list) -> bool:
    # 暴力求解，但是遇到了极端测试样例，导致超时，n^2的时间复杂度
    # n = len(nums)
    # for i in range(n):
    #     for j in range(i+1, n):
    #         if nums[i] == nums[j]:
    #             return True
    # return False

    # 先排序，n * log(n)的时间复杂度，再一次遍历，n的时间复杂度
    # n = len(nums)
    # nums[:] = sorted(nums)  # nums.sort()比sorted(nums)慢
    # for i in range(n - 1):
    #     if nums[i] == nums[i + 1]:
    #         return True
    # return False

    # 集合（时空效率均一般，但是代码简洁）
    # return len(set(nums)) != len(nums)

    # 手动建集合
    n = len(nums)
    temp_set = set()
    for i in range(n):
        if nums[i] in temp_set:
            return True
        else:
            temp_set.add(nums[i])
    return False


if __name__ == '__main__':
    value_min = 1
    value_max = 5
    len_min = 4
    len_max = 8
    nums = [random.randint(value_min, value_max) for i in range(random.randint(len_min, len_max))]
    pprint(nums)
    pprint(containsDuplicate(nums))
    pass
