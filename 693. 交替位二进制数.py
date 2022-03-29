# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-28 21:26
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个正整数，检查它的二进制表示是否总是 0、1 交替出现：换句话说，就是二进制表示中相邻两位的数字永不相同。

1 <= n <= 2^31 - 1
"""


class Solution:
    @staticmethod
    def hasAlternatingBits(n: int) -> bool:
        last_bit = n & 1
        while n > 0:
            n = n >> 1
            next_bit = n & 1
            if last_bit ^ next_bit == 0:
                return False
            last_bit = next_bit

        return True


"""
右移 1 位后，得到的新数字与原来的数字进行异或，应该得到全为 1 的二进制数 all_one = 0b111...
将这个数 + 1，可得到比原数字多 1 位的二进制数 add_one = 0b10000...
add_one & all_one 一定为 0
"""


class Solution:
    @staticmethod
    def hasAlternatingBits(n: int) -> bool:
        all_one = n ^ (n >> 1)
        return (all_one + 1) & all_one == 0


if __name__ == '__main__':
    s = Solution()

    il = [
        1,
        0b10,
        0b101,
        0b111,
        0b11010001001,
        0b1010101010101,
        0b101010101010101,
    ]

    for n in il:
        pprint(s.hasAlternatingBits(n))
    pass
