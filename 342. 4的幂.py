# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-11 13:46
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个整数，写一个函数来判断它是否是 4 的幂次方。如果是，返回 true ；否则，返回 false 。

整数 n 是 4 的幂次方需满足：存在整数 x 使得 n == 4^x

提示：

-2^31 <= n <= 2^31 - 1

进阶：你能不使用循环或者递归来完成本题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/power-of-four
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
先用 lowbit 判断是不是 2 的幂，之后判断 1 后面是否跟了偶数个 0
"""


class Solution:
    @staticmethod
    def isPowerOfFour(n: int) -> bool:
        if 0 < n == n & -n:
            count = 0
            while n != 1:
                n = n >> 1
                count += 1

            return count & 1 == 0

        else:
            return False


"""
可以构造 mask，偶数二进制位（从0开始）均为0，奇数二进制位均为1

n & mask == 0，则说明1出现在偶数二进制位，否则肯定不是4的幂
"""


class Solution1:
    @staticmethod
    def isPowerOfFour(n: int) -> bool:
        return 0 < n == n & -n and n & 0x2aaaaaaa == 0


if __name__ == '__main__':
    il = [
        16,
        5,
        1,
        8,
    ]
    s = Solution()
    for n in il:
        pprint(s.isPowerOfFour(n))
    pass
