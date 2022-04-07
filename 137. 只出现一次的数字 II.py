# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-07 10:40
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
给你一个整数数组 nums ，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次 。请你找出并返回那个只出现了一次的元素。

提示：

1 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
nums 中，除某个元素仅出现 一次 外，其余每个元素都恰出现 三次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
傻瓜解法
"""


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        counter = Counter(nums)
        for k, v in counter.items():
            if v == 1:
                return k


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> int:
        cnt = [0 for _ in range(33)]
        for num in nums:
            if num < 0:
                cnt[32] += 1
                num = -num

            for i in range(32):
                if (num >> i) & 1 == 1:
                    cnt[i] += 1

        ans = 0
        for i in range(32):
            if cnt[i] % 3 == 1:
                ans += 1 << i

        return -ans if cnt[32] % 3 == 1 else ans


if __name__ == '__main__':
    s = Solution()
    il = [
        [-2, -2, 1, 1, 4, 1, 4, 4, -4, -2],
    ]
    for nums in il:
        pprint(s.singleNumber(nums))
    pass
