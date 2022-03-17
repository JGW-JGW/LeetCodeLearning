# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-02 18:18
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个表示整数的字符串 n ，返回与它最近的回文整数（不包括自身）。如果不止一个，返回较小的那个。

“最近的”定义为两个整数差的绝对值最小。

1 <= n.length <= 18
n 只由数字组成
n 不含前导 0
n 代表在 [1, 1018 - 1] 范围内的整数
"""

"""
对于任意一个数，如12345，其最近的回文数只会从以下五种中得到：

将前一半填入后一半：12321
将前一半加一填入后一半：12421
将前一半减一填入后一半：12221
下边界：9999
上边界：100001

123456
123321
124421
122221
99999
1000001

10000
10001
10101
9999
9999
100001


从这五个数里面选取不等于原数的，且与原数差距最小的最小的数即为答案。
"""


class Solution:
    @staticmethod
    def calc_int(half_left_str: str, symmetric_flag: bool) -> int:
        n = len(half_left_str)
        result = 0
        if symmetric_flag:
            total_len = 2 * n
            for i in range(n):
                result += int(half_left_str[i]) * (10 ** i + 10 ** (total_len - i - 1))
        else:
            total_len = 2 * n - 1
            for i in range(n - 1):
                result += int(half_left_str[i]) * (10 ** i + 10 ** (total_len - i - 1))
            result += int(half_left_str[n - 1]) * 10 ** (n - 1)

        return result

    def get_candidates(self, n: str, n_len: int, n_int: int) -> List[int]:
        result_list = []
        if n_len & 1 == 1:  # 长度为奇数
            half_left_index = (n_len >> 1) + 1
            s_left = n[:half_left_index]
            s_int = self.calc_int(s_left, False)
            if s_int != n_int:
                result_list.append(s_int)

            temp = int(s_left) + 1
            if temp % 10 != 0:
                result_list.append(self.calc_int(str(temp), False))

            temp = int(s_left)
            if temp % 10 != 0:
                result_list.append(self.calc_int(str(temp - 1), False))

            result_list.append(10 ** n_len + 1)
            result_list.append(10 ** (n_len - 1) - 1)

        else:  # 长度为偶数
            half_left_index = (n_len >> 1)
            s_left = n[:half_left_index]
            s_int = self.calc_int(s_left, True)
            if s_int != n_int:
                result_list.append(s_int)

            temp = int(s_left) + 1
            if temp % 10 != 0:
                result_list.append(self.calc_int(str(temp), True))

            temp = int(s_left)
            if temp % 10 != 0:
                result_list.append(self.calc_int(str(temp - 1), True))

            result_list.append(10 ** n_len + 1)
            result_list.append(10 ** (n_len - 1) - 1)

        return result_list

    def nearestPalindromic(self, n: str) -> str:
        n_len = len(n)
        if n_len == 1:
            return '1' if n == '0' else str(int(n) - 1)
        n_int = int(n)
        candidates = self.get_candidates(n, n_len, n_int)
        index = 0
        min_abs_diff = abs(n_int - candidates[0])
        for i in range(1, len(candidates)):
            abs_diff = abs(n_int - candidates[i])
            if abs_diff < min_abs_diff:
                index = i
                min_abs_diff = abs_diff
            elif abs_diff == min_abs_diff:
                index = index if candidates[index] < candidates[i] else i

        return str(candidates[index])


if __name__ == '__main__':
    solution = Solution()
    input_list = [
        # '123',
        # '1',
        # '2',
        # '1213',
        '88',
    ]
    for item in input_list:
        pprint(solution.nearestPalindromic(item))
    pass
