# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-05 11:48
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你两个整数 left 和 right ，在闭区间 [left, right] 范围内，统计并返回 计算置位位数为质数 的整数个数。

计算置位位数 就是二进制表示中 1 的个数。

例如， 21 的二进制表示 10101 有 3 个计算置位。

提示：

1 <= left <= right <= 10^6
0 <= right - left <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/prime-number-of-set-bits-in-binary-representation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def is_valid(num: int) -> bool:
        count_of_1 = 0
        while num > 0:
            if num & 1 == 1:
                count_of_1 += 1
            num >>= 1

        return count_of_1 in {2, 3, 5, 7, 11, 13, 17, 19}

    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for num in range(left, right + 1):
            if self.is_valid(num):
                ans += 1

        return ans


if __name__ == '__main__':
    s = Solution()
    il = [
        (6, 10),
        (10, 15),
    ]
    for t in il:
        pprint(s.countPrimeSetBits(t[0], t[1]))
    pass
