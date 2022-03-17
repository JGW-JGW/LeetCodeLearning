# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-13 11:56
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
from collections import Counter

"""
给定一个整数数组 nums 和一个整数 k ，返回其中元素之和可被 k 整除的（连续、非空） 子数组 的数目。

子数组 是数组的 连续 部分。
"""

"""
前缀和：
pre_sum[i] = nums[0] + nums[1] + ... + nums[i]

连续子数组的和：
sub_sum(i, j) = nums[i] + nums[i + 1] + ... + nums[j] (0 < i < j < nums.length)

则有：
sub_sum(i, j) = pre_sum[j] - pre_sum[i - 1]

sub_sum(i, j)能否被k整除 等价于：
sub_sum(i, j) % k == 0 即：
(pre_sum[j] - pre_sum[i - 1]) % k == 0

根据同余定理：
(pre_sum[j] - pre_sum[i - 1]) % k == 0 等价于：
pre_sum[j] % k == pre_sum[i - 1] % k

最终，sub_sum(i, j)能否被k整除 等价于：
pre_sum[j] % k == pre_sum[i - 1] % k

假设pre_sum[end] % k = x (x != 0)，此时对于小于end的index，每有一个pre_sum[index] % k = x，则表明sub_sum(index, end)能被k整除。则以nums[end]结尾的符合要求的子数组个数为：满足pre_sum[index] % k = x (index < end)的所有index的个数。

当pre_sum[end] % k = 0时，此时sub_sum(0, end)符合要求，在记录时预先给定余数为0的子数组个数为1，即可套用上面的过程。

用数组记录：
mod_count[0]：pre_sum[index] % k = 0 的index的个数（初始为1）
mod_count[1]：pre_sum[index] % k = 1 的index的个数
...
mod_count[k - 1]：pre_sum[index] % k = k - 1 的index的个数
"""


class Solution:
    @staticmethod
    def subarraysDivByK(nums: List[int], k: int) -> int:
        mod_count = [0] * k
        mod_count[0], sum_of_nums, result = 1, 0, 0
        for item in nums:
            sum_of_nums += item
            mod = sum_of_nums % k
            result += mod_count[mod]
            mod_count[mod] += 1

        return result


if __name__ == '__main__':
    il = [
        ([4, 5, 0, -2, -3, 1], 5),
        ([5], 9),
    ]
    for t in il:
        s = Solution()
        pprint(s.subarraysDivByK(t[0], t[1]))
    pass
