# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-11 09:44
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个整数 n，请你判断该整数是否是 2 的幂次方。如果是，返回 true ；否则，返回 false 。

如果存在一个整数 x 使得 n == 2^x ，则认为 n 是 2 的幂次方。

提示：

-2^31 <= n <= 2^31 - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-two
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def hammingWeight(n: int) -> int:
        ans = 0
        while n != 0:
            if n & 1 == 1:
                ans += 1
            n >>= 1

        return ans

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and self.hammingWeight(n) == 1


"""
lowbit
"""


class Solution:
    @staticmethod
    def isPowerOfTwo(n: int):
        return 0 < n == (n & -n)


if __name__ == '__main__':
    pass
