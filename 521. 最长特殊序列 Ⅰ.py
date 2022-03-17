# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-05 09:25
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你两个字符串 a 和 b，请返回 这两个字符串中 最长的特殊序列  。如果不存在，则返回 -1 。

「最长特殊序列」 定义如下：该序列为 某字符串独有的最长子序列（即不能是其他字符串的子序列） 。

字符串 s 的子序列是在从 s 中删除任意数量的字符后可以获得的字符串。

例如，"abc" 是 "aebdc" 的子序列，因为删除 "aebdc" 中斜体加粗的字符可以得到 "abc" 。 "aebdc" 的子序列还包括 "aebdc" 、 "aeb" 和 "" (空字符串)。

提示：

1 <= a.length, b.length <= 100
a 和 b 由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-uncommon-subsequence-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
先判断两个字符串的长度，如果长度不相等，返回长度较长的字符串长度

如果长度相等，只要两个字符串不同，则返回字符串长度；若两个字符串相同，则返回-1
"""


class Solution:
    @staticmethod
    def findLUSlength(a: str, b: str) -> int:
        len_a = len(a)
        len_b = len(b)

        if len_a != len_b:
            return max(len_a, len_b)

        return len_a if a != b else -1


if __name__ == '__main__':
    pass
