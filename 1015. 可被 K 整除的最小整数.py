# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-10 13:57
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定正整数 k ，你需要找出可以被 k 整除的、仅包含数字 1 的最 小 正整数 n 的长度。

返回 n 的长度。如果不存在这样的 n ，就返回-1。

注意： n 不符合 64 位带符号整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/smallest-integer-divisible-by-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
小学除法：
123456 ÷ 789
1 ÷ 789 = 0 ...... 1
12 ÷ 789 = 0 ...... 12
123 ÷ 789 = 0 ...... 123
1234 ÷ 789 = 1 ...... 445
4455 ÷ 789 = 略
"""


class Solution:
    @staticmethod
    def smallestRepunitDivByK(k: int) -> int:
        if k & 1 == 0 or k % 5 == 0:
            return -1

        counter = 1
        divider = 1
        while divider % k != 0:
            counter += 1
            divider = (divider % k) * 10 + 1

        return counter


if __name__ == '__main__':
    s = Solution()
    il = [
        1,
        2,
        3,
        5,
        7,
        9
    ]

    for item in il:
        pprint(s.smallestRepunitDivByK(item))
    pass
