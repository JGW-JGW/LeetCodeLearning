# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-05 09:58
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
from math import inf

"""
给你一个整数数组 nums，和一个整数 k 。

在一个操作中，您可以选择 0 <= i < nums 的任何索引 i 。将 nums[i] 改为 nums[i] + x ，其中 x 是一个范围为 [-k, k] 的整数。对于每个索引 i ，最多 只能 应用 一次 此操作。

nums 的 分数 是 nums 中最大和最小元素的差值。 

在对nums中的每个索引最多应用一次上述操作后，返回 nums 的最低 分数 。

提示：

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^4
0 <= k <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-range-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
先求原来的分数，如果
"""


class Solution:
    @staticmethod
    def get_score_of_nums(nums: List[int]) -> int:
        max_num, min_num = nums[0], nums[0]
        for i in range(1, len(nums)):
            max_num = nums[i] if nums[i] > max_num else max_num
            min_num = nums[i] if nums[i] < min_num else min_num

        return max_num - min_num

    def smallestRangeI(self, nums: List[int], k: int) -> int:
        score = self.get_score_of_nums(nums)
        span = 2 * k

        return 0 if span >= score else score - span


class Solution1:
    @staticmethod
    def smallestRangeI(nums: List[int], k: int) -> int:
        return 0 if 2 * k >= max(nums) - min(nums) else max(nums) - min(nums) - 2 * k


if __name__ == '__main__':
    solution = Solution()
    input_list = [
        ([0], 0),
        ([0, 10], 2),
        ([1, 3, 6], 3),
    ]
    for item in input_list:
        pprint(solution.smallestRangeI(item[0], item[1]))
    pass
