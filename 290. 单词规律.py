# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-02-25 21:27
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一种规律 pattern 和一个字符串 s ，判断 s 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

提示:

1 <= pattern.length <= 300
pattern 只包含小写英文字母
1 <= s.length <= 3000
s 只包含小写英文字母和 ' '
s 不包含 任何前导或尾随对空格
s 中每个单词都被 单个空格 分隔

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/word-pattern
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
用字典
"""


class Solution:
    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        item_list = s.split()

        n_pattern = len(pattern)
        n_item = len(item_list)

        if n_item != n_pattern:
            return False

        pattern2item = {}
        item2pattern = {}

        for char, item in zip(pattern, item_list):
            if (item in item2pattern and item2pattern[item] != char) or (
                    char in pattern2item and pattern2item[char] != item):
                return False
            pattern2item[char] = item
            item2pattern[item] = char

        return True


class Solution1:
    @staticmethod
    def wordPattern(pattern: str, s: str) -> bool:
        item_list = s.split()

        n_pattern = len(pattern)
        n_item = len(item_list)

        if n_item != n_pattern:
            return False

        return len(set(zip(pattern, item_list))) == len(set(pattern)) == len(set(item_list))


if __name__ == '__main__':
    s = Solution()

    input_list = [
        ('abb', 'd c c'),
        ('abba', 'ab ba ba aba'),
        ('abba', 'dog dog dog dog')
    ]

    for item in input_list:
        pprint(s.wordPattern(item[0], item[1]))
    pass
