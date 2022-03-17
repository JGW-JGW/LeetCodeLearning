# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-03 18:28
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。返回这个结果。

0 <= num <= 2^31 - 1
"""


class Solution:
    @staticmethod
    def get_sum_of_digits(num: int) -> int:
        result = 0
        while num > 0:
            num, mod = divmod(num, 10)
            result += mod

        return result

    def addDigits(self, num: int) -> int:
        result = self.get_sum_of_digits(num)
        while result >= 10:
            result = self.get_sum_of_digits(result)

        return result


"""
https://leetcode-cn.com/problems/add-digits/solution/ge-wei-xiang-jia-by-leetcode-solution-u4kj/

num 与其各位相加的结果模 9 同余。
"""


class Solution1(object):
    @staticmethod
    def addDigits(num: int) -> int:
        if num == 0:
            return 0

        mod = num % 9

        return 9 if mod == 0 else mod


if __name__ == '__main__':
    # solution = Solution()
    solution = Solution1()
    input_list = [
        123456,
        1232345,
        123,
    ]

    for item in input_list:
        pprint('================')
        # pprint(solution.get_sum_of_digits(item))
        pprint(solution.addDigits(item))

    pass
