# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-05 15:16
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
from math import inf
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你两个数组 nums1 和 nums2 。

请你返回 nums1 和 nums2 中两个长度相同的 非空 子序列的最大点积。

数组的非空子序列是通过删除原数组中某些元素（可能一个也不删除）后剩余数字组成的序列，但不能改变数字间相对顺序。比方说，[2,3,5] 是 [1,2,3,4,5] 的一个子序列而 [1,5,3] 不是。

提示：

1 <= nums1.length, nums2.length <= 500
-1000 <= nums1[i], nums2[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-dot-product-of-two-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
假设只使用数组 nums1 的前 i+1 个元素（0至i）以及数组 nums2 的前 j+1 个元素（0至j）时，可以获得的非空子序列最大点积记作 f[i][j]

如果nums1[i]和nums2[j]同时被选中，将 nums1[i] * nums2[j] 记作 xij，此时有 f[i][j] = max(f[i-1][j-1] + xij, xij)

如果nums1[i]和nums2[j]没有同时被选中，则最多只能选择其中一个数字（如果两个数字都参与了点积，那么就会与这两个数字分别是各自所在数组的最后一个元素相矛盾），三种情况分别为：扔掉nums1[i]；扔掉nums2[j]；扔掉两者，此时有：f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1])

另外考虑到f[i-1][j] = max(f[i-2][j], f[i-1][j-1], ...)当中已经考虑了f[i-1][j-1]，所以f[i][j]可以简化为：
f[i][j] = max(f[i-1][j-1] + xij, xij, f[i-1][j], f[i][j-1])

当i = 0时，索引i-1为负数，相关的项需要删掉
当j = 0时，索引j-1为负数，相关的项需要删掉
"""


class Solution:
    @staticmethod
    def maxDotProduct(nums1: List[int], nums2: List[int]) -> int:
        n1, n2 = len(nums1), len(nums2)
        f = [[-50000001 for _ in range(n2 + 1)] for _ in range(n1 + 1)]
        # f = [[-50000001] * (n2 + 1)] * (n1 + 1)

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                v = nums1[i - 1] * nums2[j - 1]
                f[i][j] = max(v, f[i - 1][j], f[i][j - 1], v + f[i - 1][j - 1])

        return f[n1][n2]


class Solution:
    @staticmethod
    def maxDotProduct(nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)
        # dp = [[-inf] * (n + 1) for _ in range(m + 1)]
        dp = [[-inf] * (n + 1)] * (m + 1)
        for i in range(m):
            for j in range(n):
                v = nums1[i] * nums2[j]
                dp[i + 1][j + 1] = max(max(0, dp[i][j]) + v, dp[i + 1][j], dp[i][j + 1])
        return dp[-1][-1]


if __name__ == '__main__':
    solution = Solution()

    input_list = [
        # ([2, 1, -2, 5], [3, 0, -6]),
        ([3, -2], [2, -6, 7]),
        # ([-1, -1], [1, 1]),
    ]

    for t in input_list:
        pprint(solution.maxDotProduct(t[0], t[1]))

    pass
