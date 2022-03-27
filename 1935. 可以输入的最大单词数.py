# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-26 18:52
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
键盘出现了一些故障，有些字母键无法正常工作。而键盘上所有其他键都能够正常工作。

给你一个由若干单词组成的字符串 text ，单词间由单个空格组成（不含前导和尾随空格）；另有一个字符串 brokenLetters ，由所有已损坏的不同字母键组成，返回你可以使用此键盘完全输入的 text 中单词的数目。

提示：

1 <= text.length <= 10^4
0 <= brokenLetters.length <= 26
text 由若干用单个空格分隔的单词组成，且不含任何前导和尾随空格
每个单词仅由小写英文字母组成
brokenLetters 由 互不相同 的小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-words-you-can-type
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
暴力
"""


class Solution:
    @staticmethod
    def canBeTypedWords(text: str, broken_letters: str) -> int:
        broken_set = set(broken_letters)
        count = 0
        for word in text.split():
            flag = True  # True 表示 word 可以正常输入
            for char in word:
                if char in broken_set:
                    flag = False
                    break
            if flag:
                count += 1

        return count


if __name__ == '__main__':
    il = [
        ("hello world", "ad"),
        ("leet code", "lt"),
    ]
    s = Solution()
    for t in il:
        pprint(s.canBeTypedWords(t[0], t[1]))
    pass
