# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-10 16:50
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
from collections import Counter

"""
给定一个整数数组 nums，其中恰好有两个元素只出现一次，其余所有元素均出现两次。 找出只出现一次的那两个元素。你可以按 任意顺序 返回答案。

 

进阶：你的算法应该具有线性时间复杂度。你能否仅使用常数空间复杂度来实现？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/single-number-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> List[int]:
        counter = Counter(nums)
        result_list = []
        count = 0
        for key, value in counter.items():
            if count == 2:
                break
            if value == 1:
                result_list.append(key)
                count += 1

        return result_list


class Solution:
    @staticmethod
    def singleNumber(nums: List[int]) -> List[int]:
        xor = nums[0]
        n = len(nums)
        for index in range(1, n):
            xor = xor ^ nums[index]

        mask = xor & -xor

        result_list = [0, 0]

        for item in nums:
            if item & mask == 0:
                result_list[0] ^= item
            else:
                result_list[1] ^= item

        return result_list


if __name__ == '__main__':
    s = Solution()
    il = [
        [1, 2, 1, 3, 2, 5],
        [-1, 0],
        [0, 1],
    ]
    for item in il:
        pprint(s.singleNumber(item))
    pass
