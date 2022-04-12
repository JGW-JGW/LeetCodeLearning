# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-11 17:12
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
from math import log2
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
对整数的二进制表示取反（0 变 1 ，1 变 0）后，再转换为十进制表示，可以得到这个整数的补数。

例如，整数 5 的二进制表示是 "101" ，取反后得到 "010" ，再转回十进制表示得到补数 2 。
给你一个整数 num ，输出它的补数。

提示：

1 <= num < 2^31

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-complement
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def findComplement(num: int) -> int:
        ans = 0
        count = 0
        while num != 0:
            if num & 1 == 0:
                ans += 1 << count
            count += 1
            num >>= 1

        return ans


"""
彤哥的思路：

1 - 找到最高位的 1，生成一个该最高位至最低位全为 1 的二进制数
2 - 将生成的二进制数 异或 原始数字
"""


class Solution:
    @staticmethod
    def findComplement(num: int) -> int:
        highest_bit = 0
        x = num
        while x != 0:
            # 找最低位（最右边）的 1
            highest_bit = x & -x
            # 干掉最右边的 1
            x = x & (x - 1)

        return num ^ ((highest_bit << 1) - 1)


"""
数学方法直接求出最高位
"""


class Solution:
    @staticmethod
    def findComplement(num: int) -> int:
        return num ^ ((1 << (int(log2(num)) + 1)) - 1)


if __name__ == '__main__':
    il = [
        5,
        1,
    ]
    s = Solution()
    for num in il:
        pprint(s.findComplement(num))
    pass
