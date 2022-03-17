# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-06 11:12
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个字符串 s，它仅由字母 'a' 和 'b' 组成。每一次删除操作都可以从 s 中删除一个回文 子序列。

返回删除给定字符串中所有字符（字符串为空）的最小删除次数。

「子序列」定义：如果一个字符串可以通过删除原字符串某些字符而不改变原字符顺序得到，那么这个字符串就是原字符串的一个子序列。

「回文」定义：如果一个字符串向后和向前读是一致的，那么这个字符串就是一个回文。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-palindromic-subsequences
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
其实是一道脑筋急转弯

子序列可以不连续，如果不能一次删除，那最多两次（先删所有a，再删所有b）
"""


class Solution:
    @staticmethod
    def removePalindromeSub(s: str) -> int:
        return 2 if s[::-1] != s else 1


if __name__ == '__main__':
    pass
