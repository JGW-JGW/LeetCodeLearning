# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-10 15:56
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
如果数组是单调递增或单调递减的，那么它是 单调 的。

如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i]> = nums[j]，那么数组 nums 是单调递减的。

当给定的数组 nums 是单调数组时返回 true，否则返回 false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/monotonic-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def isMonotonic(nums: List[int]) -> bool:
        first_flag = 0
        n = len(nums)
        for index in range(n - 1):
            if first_flag > 0:
                if nums[index + 1] < nums[index]:
                    return False

            elif first_flag < 0:
                if nums[index + 1] > nums[index]:
                    return False

            else:  # first_flag == 0
                if nums[index + 1] > nums[index]:
                    first_flag = 1
                elif nums[index + 1] < nums[index]:
                    first_flag = -1

        return True


if __name__ == '__main__':
    s = Solution()
    il = [
        [1, 2, 2, 3],
        [6, 5, 4, 4],
        [1, 3, 2],
    ]
    for item in il:
        pprint(s.isMonotonic(item))
    pass
