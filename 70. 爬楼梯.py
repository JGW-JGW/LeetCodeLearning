# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-26 12:19
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
from math import sqrt
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

提示：

1 <= n <= 45
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)


"""
上面的递归方式，超时了

既然是个斐波那契数列，那干脆套公式
"""


class Solution:
    @staticmethod
    def nth_of_fibonacci(n: int) -> int:
        return int(1 / sqrt(5) * (((1 + sqrt(5)) / 2) ** n - ((1 - sqrt(5)) / 2) ** n))

    def climbStairs(self, n: int) -> int:
        return self.nth_of_fibonacci(n + 1)


if __name__ == '__main__':
    s = Solution()
    il = [
        # 2,
        # 3,
        44,
    ]
    for n in il:
        pprint(s.climbStairs(n))
    pass
