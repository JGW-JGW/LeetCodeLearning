# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.11 09:57
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random

"""
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:

输入: [2,2,1]
输出: 1
示例 2:

输入: [4,1,2,1,2]
输出: 4

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x21ib6/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def singleNumber(nums: List[int]) -> int:
    # 先排序，再遍历
    # n = len(nums)
    # nums[:] = sorted(nums)
    # i = 0
    # while i <= n - 2:
    #     if nums[i] == nums[i + 1]:
    #         i += 2
    #     else:
    #         return nums[i]
    # if i == n - 1:
    #     return nums[-1]

    # 集合
    # temp_set = set()
    # len_nums = len(nums)
    # for i in range(len_nums):
    #     if nums[i] in temp_set:
    #         temp_set.remove(nums[i])
    #     else:
    #         temp_set.add(nums[i])
    # return temp_set.pop()

    # 异或运算均有交换律
    len_nums = len(nums)
    result = 0
    for i in range(len_nums):
        result ^= nums[i]
    return result


if __name__ == '__main__':
    nums = [1, 2, 1, 2, 3]
    print(singleNumber(nums))
    pass
