# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-11 14:16
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你两个整数 a 和 b ，不使用 运算符 + 和 - ，计算并返回两整数之和。

提示：

-1000 <= a, b <= 1000
"""


class Solution:
    @staticmethod
    def getSum(a: int, b: int) -> int:
        return sum([a, b])


"""
以上方法过于偷懒，显然不太行

还是应该采用位运算
"""


class Solution:
    @staticmethod
    def getSum(a: int, b: int) -> int:
        # 保留一个整数的二进制表示的后32位的方法：将该数与 0xffffffff 进行 与 计算
        mask = 0x100000000
        mask32 = 0xffffffff
        mask_sign = 0x80000000

        if b == 0:
            return a

        while b != 0:
            carry = (a & b) << 1
            # a = (a ^ b) % mask
            # b = carry % mask
            a = (a ^ b) & mask32
            b = carry & mask32

        if a & mask_sign:  # 为负数
            return ~(a ^ mask32)
        else:
            return a


if __name__ == '__main__':
    il = [
        # (1, 2),
        # (2, 3),
        (-1, 0),
        (0, -1),
        (-1, -1),
        (-3, -123)
    ]
    s = Solution()
    for t in il:
        pprint(s.getSum(t[0], t[1]))
    pass
