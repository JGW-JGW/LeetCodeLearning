# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-02-24 14:31
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

0 <= s.length <= 5 * 10^4
s 由英文字母、数字、符号和空格组成
"""


class Solution:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        n = len(s)
        result = []
        max_length = 0
        cur_length = 0
        for i in range(n):
            if s[i] not in result:
                result.append(s[i])
                cur_length += 1
            else:  # s[i] is at index m
                m = result.index(s[i])
                result = result[m + 1:]
                result.append(s[i])
                cur_length = len(result)
            max_length = max(max_length, cur_length)

        return max_length


class Solution1:
    @staticmethod
    def lengthOfLongestSubstring(s: str) -> int:
        n = len(s)
        char_set = set()  # 记录每个字符是否出现过
        max_length = 0
        cur_index = 0

        for i in range(n):
            if i > 0:
                char_set.remove(s[i - 1])
            while cur_index < n and s[cur_index] not in char_set:
                char_set.add(s[cur_index])
                cur_index += 1
            max_length = max(max_length, cur_index - i)

        return max_length


if __name__ == '__main__':
    s = Solution1()
    input_list = [
        'aab',
        # 'abcabcbb',
        # 'bbbbb',
        # 'pwwkew',
    ]
    for item in input_list:
        pprint(s.lengthOfLongestSubstring(item))
    pass
