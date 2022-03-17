# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-02-25 20:24
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict, Tuple
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
复数 可以用字符串表示，遵循 "实部+虚部i" 的形式，并满足下述条件：

实部 是一个整数，取值范围是 [-100, 100]
虚部 也是一个整数，取值范围是 [-100, 100]
i^2 == -1
给你两个字符串表示的复数 num1 和 num2 ，请你遵循复数表示形式，返回表示它们乘积的字符串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/complex-number-multiplication
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
  (a + bi)(c + di)
= ac - bd + (ad + bc)i
"""


class Solution:
    @staticmethod
    def get_real_imag_of_num(num: str) -> Tuple[int, int]:
        plus_index = num.index('+')
        real = int(num[:plus_index])
        imag = int(num[plus_index + 1:-1])
        return real, imag

    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imag1 = self.get_real_imag_of_num(num1)
        real2, imag2 = self.get_real_imag_of_num(num2)
        real = real1 * real2 - imag1 * imag2
        imag = real1 * imag2 + real2 * imag1
        return '{}+{}i'.format(real, imag)


class Solution1:
    @staticmethod
    def complexNumberMultiply(num1: str, num2: str) -> str:
        plus_index = num1.index('+')
        real1, imag1 = int(num1[:plus_index]), int(num1[plus_index + 1:-1])
        plus_index = num2.index('+')
        real2, imag2 = int(num2[:plus_index]), int(num2[plus_index + 1:-1])
        real = real1 * real2 - imag1 * imag2
        imag = real1 * imag2 + real2 * imag1
        return '{}+{}i'.format(real, imag)


class Solution2:
    @staticmethod
    def complexNumberMultiply(num1: str, num2: str) -> str:
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))
        return f'{real1 * real2 - imag1 * imag2}+{real1 * imag2 + imag1 * real2}i'


if __name__ == '__main__':
    solution = Solution()

    input_list = [
        '1+-4i',
        '-1+3i'
    ]

    for item in input_list:
        pprint(solution.get_real_imag_of_num(item))
