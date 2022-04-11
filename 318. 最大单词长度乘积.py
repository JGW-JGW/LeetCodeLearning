# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-11 10:21
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个字符串数组 words ，找出并返回 length(words[i]) * length(words[j]) 的最大值，并且这两个单词不含有公共字母。如果不存在这样的两个单词，返回 0 。

提示：

2 <= words.length <= 1000
1 <= words[i].length <= 1000
words[i] 仅包含小写字母

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
暴力法
"""


class Solution:
    @staticmethod
    def have_common_letter(word1: str, word2: str) -> bool:
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        for char in word1:
            if char in word2:
                return True

        return False

    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if not self.have_common_letter(words[i], words[j]):
                    product = len(words[i]) * len(words[j])
                    ans = product if product > ans else ans

        return ans


if __name__ == '__main__':
    il = [
        ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"],
        ["a", "ab", "abc", "d", "cd", "bcd", "abcd"],
        ["a", "aa", "aaa", "aaaa"],
    ]
    s = Solution()
    for words in il:
        pprint(s.maxProduct(words))

    pass
