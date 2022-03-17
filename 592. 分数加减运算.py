# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-10 21:08
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict, Tuple
import random as rd
from math import gcd
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个表示分数加减运算的字符串 expression ，你需要返回一个字符串形式的计算结果。 

这个结果应该是不可约分的分数，即最简分数。 如果最终结果是一个整数，例如 2，你需要将它转换成分数形式，其分母为 1。所以在上述例子中, 2 应该被转换为 2/1。

提示:

输入和输出字符串只包含 '0' 到 '9' 的数字，以及 '/', '+' 和 '-'。 
输入和输出分数格式均为 ±分子/分母。如果输入的第一个分数或者输出的分数是正数，则 '+' 会被省略掉。
输入只包含合法的最简分数，每个分数的分子与分母的范围是  [1,10]。 如果分母是1，意味着这个分数实际上是一个整数。
输入的分数个数范围是 [1,10]。
最终结果的分子与分母保证是 32 位整数范围内的有效整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fraction-addition-and-subtraction
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # @staticmethod
    # def lcm(x: int, y: int) -> int:
    #     m, n = max(x, y), min(x, y)
    #     while m % n != 0:
    #         m, n = n, m % n
    #
    #     return x * y // n
    #
    # @staticmethod
    # def gcd(x: int, y: int) -> int:
    #     m, n = max(x, y), min(x, y)
    #     while m % n != 0:
    #         m, n = n, m % n
    #
    #     return n

    @staticmethod
    def lcm(x: int, y: int) -> int:
        return x * y // gcd(x, y)

    def multi_lcm(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        lcm0 = self.lcm(nums[0], nums[1])
        for index in range(2, n):
            lcm0 = self.lcm(lcm0, nums[index])

        return lcm0

    @staticmethod
    def get_numerators_and_denominators(expression: str) -> Tuple[List[int], List[int]]:
        numerators = []
        denominators = []

        temp = expression.split('/')

        numerators.append(int(temp[0]))

        for index in range(1, len(temp) - 1):
            if '+' in temp[index]:
                temp_temp = temp[index].split('+')
                numerators.append(int(temp_temp[1]))
                denominators.append(int(temp_temp[0]))
            else:
                temp_temp = temp[index].split('-')
                numerators.append(-int(temp_temp[1]))
                denominators.append(int(temp_temp[0]))

        denominators.append(int(temp[-1]))

        return numerators, denominators

    def fractionAddition(self, expression: str) -> str:
        numerators, denominators = self.get_numerators_and_denominators(expression)
        lcm0 = self.multi_lcm(denominators)
        sum_of_numerators = 0

        for index in range(len(numerators)):
            sum_of_numerators += numerators[index] * lcm0 // denominators[index]

        char_list = []

        gcd0 = gcd(sum_of_numerators, lcm0)

        char_list.append(str(sum_of_numerators // gcd0))
        char_list.append('/')
        char_list.append(str(lcm0 // gcd0))

        return "".join(char_list)


if __name__ == '__main__':
    s = Solution()

    il = [
        # "-1/2+1/2",
        # "-1/2+1/2+1/3",
        # "1/3-1/2",
        "-7/3",
    ]

    for item in il:
        pprint(s.fractionAddition(item))
    pass
