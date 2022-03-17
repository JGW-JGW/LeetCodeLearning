# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.11 17:51
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2ba4i/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    # 先删了所有0，记住删了多少个0，再拼上多少个0，时空效率略低
    # n = len(nums)
    # counter = 0
    # i = 0
    # while i < n:
    #     if nums[i] == 0:
    #         counter += 1
    #         del nums[i]
    #         n -= 1
    #     else:
    #         i += 1
    # nums.extend([0 for i in range(counter)])

    # 双指针
    slow = 0
    fast = 1
    while fast < len(nums):
        if nums[slow] == 0 and nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1
        elif nums[slow] != 0:
            slow += 1
        fast += 1

    # 抄袭，发现和上面的那个没啥差别，甚至更慢
    # fast = 0
    # slow = 0
    # while fast < len(nums):
    #     if nums[fast] != 0:
    #         nums[slow], nums[fast] = nums[fast], nums[slow]
    #         slow += 1
    #     fast += 1


if __name__ == '__main__':
    nums = [random.randint(0, 1) for i in range(random.randint(7, 10))]
    # nums = [1, 1, 1, 0, 0, 0, 1]
    pprint(nums)
    moveZeroes(nums)
    pprint(nums)

    pass
