# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-26 11:28
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
提示：

n == nums.length
1 <= n <= 10^4
0 <= nums[i] <= n
nums 中的所有数字都 独一无二

进阶：你能否实现线性时间复杂度、仅使用额外常数空间的算法解决此问题?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/missing-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def missingNumber(nums: List[int]) -> int:
        n = len(nums)
        sum_0_to_n = n * (n + 1) // 2
        sum_nums = sum(nums)

        return sum_0_to_n - sum_nums


if __name__ == '__main__':
    s = Solution()
    il = [
        [3, 0, 1],
        [0, 1],
    ]

    for nums in il:
        pprint(s.missingNumber(nums))

    pass
