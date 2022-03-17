# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-02-26 08:59
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个下标从 0 开始的整数数组 nums ，该数组的大小为 n ，请你计算 nums[j] - nums[i] 能求得的 最大差值 ，其中 0 <= i < j < n 且 nums[i] < nums[j] 。

返回 最大差值 。如果不存在满足要求的 i 和 j ，返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-difference-between-increasing-elements
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。、

提示：

n == nums.length
2 <= n <= 1000
1 <= nums[i] <= 10^9
"""


class Solution:
    @staticmethod
    def maximumDifference(nums: List[int]) -> int:
        n = len(nums)
        max_diff = -1
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[j] <= nums[i]:
                    continue
                else:
                    max_diff = max(max_diff, nums[j] - nums[i])
        return max_diff


class Solution1:
    @staticmethod
    def maximumDifference(nums: List[int]) -> int:
        n = len(nums)
        max_diff = -1
        min_before_j = nums[0]
        for j in range(1, n):
            if nums[j] > min_before_j:
                max_diff = max(max_diff, nums[j] - min_before_j)
            else:
                min_before_j = nums[j]

        return max_diff


if __name__ == '__main__':
    solution = Solution1()
    input_list = [
        # [2, 59, 37, 57, 10, 30],
        [7, 1, 5, 4]
    ]
    for item in input_list:
        pprint(solution.maximumDifference(item))
    pass
