# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-26 17:09
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个长度为 n 、下标从 1 开始的二进制字符串，所有位最开始都是 0 。我们会按步翻转该二进制字符串的所有位（即，将 0 变为 1）。

给你一个下标从 1 开始的整数数组 flips ，其中 flips[i] 表示对应下标 i 的位将会在第 i 步翻转。

二进制字符串 前缀一致 需满足：在第 i 步之后，在 闭 区间 [1, i] 内的所有位都是 1 ，而其他位都是 0 。

返回二进制字符串在翻转过程中 前缀一致 的次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-times-binary-string-is-prefix-aligned
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

提示：

n == flips.length
1 <= n <= 5 * 10^4
flips 是范围 [1, n] 中所有整数构成的一个排列
"""

"""
求和
"""


class Solution:
    @staticmethod
    def numTimesAllBlue(flips: List[int]) -> int:
        n = len(flips)
        sum_of_indexes = 0
        sum_of_nums = 0
        count = 0
        for i in range(n):
            sum_of_indexes += i + 1
            sum_of_nums += flips[i]
            if sum_of_indexes == sum_of_nums:
                count += 1

        return count


if __name__ == '__main__':
    s = Solution()
    il = [
        [3, 2, 4, 1, 5],
        [4, 1, 2, 3],
    ]
    for flips in il:
        pprint(s.numTimesAllBlue(flips))
    pass
