# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-11 13:26
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个整数 n ，对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，返回一个长度为 n + 1 的数组 ans 作为答案。

提示：

0 <= n <= 10^5

进阶：

很容易就能实现时间复杂度为 O(n log n) 的解决方案，你可以在线性时间复杂度 O(n) 内用一趟扫描解决此问题吗？
你能不使用任何内置函数解决此问题吗？（如，C++ 中的 __builtin_popcount ）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/counting-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
汉明重量
"""


class Solution:
    @staticmethod
    def calc_hamming_weight(n: int) -> int:
        ans = 0
        while n != 0:
            if n & 1 == 1:
                ans += 1
            n = n >> 1

        return ans

    def countBits(self, n: int) -> List[int]:
        i = 0
        ans = []
        while i <= n:
            ans.append(self.calc_hamming_weight(i))
            i += 1

        return ans


"""
由于考虑 0 ~ n 的连续整数，则可以找出递推关系

奇数比上一个偶数多了一个 1

偶数的 1 的个数与该偶数右移 1 位的数具有相同数量的 1
"""


class Solution:
    @staticmethod
    def countBits(n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            if i & 1 == 1:
                ans[i] = ans[i - 1] + 1
            else:
                ans[i] = ans[i >> 1]

        return ans


if __name__ == '__main__':
    il = [
        2,
        5,
    ]
    s = Solution()
    for n in il:
        pprint(s.countBits(n))
    pass
