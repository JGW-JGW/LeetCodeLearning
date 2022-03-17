# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-02-27 10:58
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一组正整数，相邻的整数之间将会进行浮点除法操作。例如， [2,3,4] -> 2 / 3 / 4 。

但是，你可以在任意位置添加任意数目的括号，来改变算数的优先级。你需要找出怎么添加括号，才能得到最大的结果，并且返回相应的字符串格式的表达式。你的表达式不应该含有冗余的括号。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/optimal-division
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入数组的长度在 [1, 10] 之间。
数组中每个元素的大小都在 [2, 1000] 之间。
每个测试用例只有一个最优除法解。
"""

"""
只有一种情况最大
a/(b/c/d/e/...) = a * c * d * e * f * ... / b
"""


class Solution:
    def f(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return "{}".format(nums[0])
        elif n == 2:
            return "{}/{}".format(nums[0], nums[1])
        elif n == 3:
            return "{}/({}/{})".format(nums[0], nums[1], nums[2])
        else:  # 4 <= n <= 10
            return "{}/{}".format(nums[0], self.g(nums[1:]))

    def g(self, nums: List[int]) -> str:
        n = len(nums)
        if n == 3:
            return "({}/{}/{})".format(nums[0], nums[1], nums[2])
        else:  # 4 <= n <= 10
            return "({}/{})".format(nums[0], self.f(nums[1:]))

    def optimalDivision(self, nums: List[int]) -> str:
        return self.f(nums)


class Solution1:
    @staticmethod
    def optimalDivision(nums: List[int]) -> str:
        n = len(nums)
        if n == 1:
            return "{}".format(nums[0])
        elif n == 2:
            return "{}/{}".format(nums[0], nums[1])
        else:  # 3 <= n <= 10
            return "{}/({}/{})".format(
                nums[0],
                nums[1],
                "/".join([str(item) for item in nums[2:]])
            )


if __name__ == '__main__':
    solution = Solution1()

    n_input = 0
    input_list = [[] for _ in range(n_input)]

    for item in input_list:
        n_random = rd.randint(1, 10)
        for _ in range(n_random):
            num_random = rd.randint(2, 1000)
            item.append(num_random)

    input_list.extend([
        [1000, 1000, 10, 2],
        [6, 2, 3, 4, 5],
    ])

    for item in input_list:
        pprint(solution.optimalDivision(item))
    pass
