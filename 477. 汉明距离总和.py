# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-12 19:42
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
两个整数的 汉明距离 指的是这两个数字的二进制数对应位不同的数量。

给你一个整数数组 nums，请你计算并返回 nums 中任意两个数之间 汉明距离的总和 。

提示：

1 <= nums.length <= 10^4
0 <= nums[i] <= 10^9
给定输入的对应答案符合 32-bit 整数范围

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/total-hamming-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def calc_hamming_weight(n: int) -> int:
        n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
        n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff)
        n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)

        return n

    def calc_hamming_distance(self, a: int, b: int) -> int:
        return self.calc_hamming_weight(a ^ b)

    def totalHammingDistance(self, nums: List[int]) -> int:
        counter = Counter(nums)
        keys = list(counter.keys())
        n = len(keys)
        ans = 0
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                ans += self.calc_hamming_distance(keys[i], keys[j]) * counter[keys[i]] * counter[keys[j]]

        return ans


"""
上述方法，超时，参考宫水三叶大佬的思路

从 0 ~ 31 位，每个位置在统计汉明距离之和时可以独立进行

每个位置贡献的汉明距离和为：该位置上 0 的个数 × 该位置上 1 的个数
"""


class Solution:
    @staticmethod
    def totalHammingDistance(nums: List[int]) -> int:
        num_of_0 = [0] * 32
        num_of_1 = [0] * 32
        for num in nums:
            for mask in range(32):
                if num & (1 << mask):
                    num_of_1[mask] += 1
                else:
                    num_of_0[mask] += 1

        ans = 0
        for i in range(32):
            ans += num_of_0[i] * num_of_1[i]

        return ans


"""
调整一下内外循环的顺序
"""


class Solution:
    @staticmethod
    def totalHammingDistance(nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            n_of_0, n_of_1 = 0, 0
            for num in nums:
                if num & (1 << i):
                    n_of_1 += 1
                else:
                    n_of_0 += 1

            ans += n_of_0 * n_of_1

        return ans


if __name__ == '__main__':
    il = [
        [4, 14, 2],
        [4, 14, 4],
        [9, 9, 0, 5, 6],
    ]
    s = Solution()
    for nums in il:
        pprint(s.totalHammingDistance(nums))
    pass
