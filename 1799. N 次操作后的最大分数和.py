# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-22 20:32
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你 nums ，它是一个大小为 2 * n 的正整数数组。你必须对这个数组执行 n 次操作。

在第 i 次操作时（操作编号从 1 开始），你需要：

选择两个元素 x 和 y 。
获得分数 i * gcd(x, y) 。
将 x 和 y 从 nums 中删除。
请你返回 n 次操作后你能获得的分数和最大为多少。

函数 gcd(x, y) 是 x 和 y 的最大公约数。

提示：

1 <= n <= 7
nums.length == 2 * n
1 <= nums[i] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximize-score-after-n-operations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def gcd(m: int, n: int) -> int:
    while n != 0:
        m, n = n, m % n

    return m


def count_1_in_binary(n: int) -> int:
    count = 0
    while n:
        n = (n - 1) & n
        count += 1

    return count


class Solution:
    @staticmethod
    def maxScore(nums: List[int]) -> int:
        n = len(nums)

        # 提前计算 gcd 矩阵，用来查表
        gcd_mat = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n - 1):
            for j in range(i + 1, n):
                gcd_mat[i][j] = gcd(nums[i], nums[j])

        # 数量上限先求出来
        n_state = 1 << n

        # 用来记录不同状态码的得分
        dp = [0 for _ in range(n_state)]

        # 针对所有状态码进行遍历
        for state_code in range(3, n_state):
            count = count_1_in_binary(state_code)
            if count & 1 == 0:
                operation = count >> 1
                flag = False
                for i in range(n - 1):
                    for j in range(i + 1, n):
                        if (state_code >> i) & 1 and (state_code >> j) & 1:
                            dp[state_code] = max(
                                dp[state_code],
                                dp[state_code - (1 << i) - (1 << j)] + operation * gcd_mat[i][j]
                            )

        return dp[n_state - 1]


if __name__ == '__main__':
    s = Solution()
    il = [
        [1, 2],
        [3, 4, 6, 8],
        [1, 2, 3, 4, 5, 6],
    ]
    for nums in il:
        pprint(s.maxScore(nums))
    pass
