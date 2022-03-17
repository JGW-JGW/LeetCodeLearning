# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-16 12:18
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
输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。

限制：

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^6
"""


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        counter = Counter(nums)
        for key in counter:
            diff = target - key
            if diff != key:
                if diff in counter:
                    return [key, diff]
            elif counter[key] > 1:
                return [key, key]


class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [nums[i], nums[j]]
        return []


if __name__ == '__main__':
    il = [
        ([2, 7, 11, 15], 9),
        ([10, 26, 30, 31, 47, 60], 40),
    ]

    s = Solution()

    for t in il:
        pprint(s.twoSum(t[0], t[1]))

    pass
