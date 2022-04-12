# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-11 16:28
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。

提示：

0 <= x, y <= 2^31 - 1
"""


class Solution:
    @staticmethod
    def hammingWeight(n: int) -> int:
        n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
        n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff)
        n = (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)

        return n

    def hammingDistance(self, x: int, y: int) -> int:
        return self.hammingWeight(x ^ y)


if __name__ == '__main__':
    il = [
        (1, 4),
        (3, 1)
    ]
    s = Solution()
    for t in il:
        pprint(s.hammingDistance(t[0], t[1]))
    pass
