# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-17 14:24
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个只包含字符 'a'，'b' 和 'c' 的字符串 s ，你可以执行下面这个操作（5 个步骤）任意次：

选择字符串 s 一个 非空 的前缀，这个前缀的所有字符都相同。
选择字符串 s 一个 非空 的后缀，这个后缀的所有字符都相同。
前缀和后缀在字符串中任意位置都不能有交集。
前缀和后缀包含的所有字符都要相同。
同时删除前缀和后缀。
请你返回对字符串 s 执行上面操作任意次以后（可能 0 次），能得到的 最短长度 。

提示：

1 <= s.length <= 10^5
s 只包含字符 'a'，'b' 和 'c' 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-length-of-string-after-deleting-similar-ends
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
双指针
"""


class Solution:
    @staticmethod
    def is_deletable(s: str, n: int) -> bool:
        return n > 1 and s[0] == s[-1]

    @staticmethod
    def get_left_continuous_length(s: str, n: int) -> int:
        count = 1
        while count < n:
            if s[count] == s[0]:
                count += 1
            else:
                break

        return count

    @staticmethod
    def get_right_continuous_length(s: str, n: int) -> int:
        index = n - 2
        while index >= 0:
            if s[index] == s[n - 1]:
                index -= 1
            else:
                break

        return n - index - 1

    def minimumLength(self, s: str) -> int:
        n = len(s)
        if not self.is_deletable(s, n):
            return n

        # 求左侧连续的相同字符的长度
        left_count = self.get_left_continuous_length(s, n)

        # 如果这个长度等于 n，说明 s 由相同的字符构成，一定可以删掉
        if left_count == n:
            return 0

        # 求右侧连续的相同字符的长度
        right_count = self.get_right_continuous_length(s, n)

        return self.minimumLength(s[left_count:(n - right_count)])


class Solution:
    @staticmethod
    def minimumLength(s: str) -> int:
        left_pointer, right_pointer = 0, len(s) - 1
        while left_pointer < right_pointer:
            if s[left_pointer] != s[right_pointer]:
                break
            char = s[left_pointer]
            while left_pointer <= right_pointer and s[left_pointer] == char:
                left_pointer += 1
            while left_pointer <= right_pointer and s[right_pointer] == char:
                right_pointer -= 1

        return right_pointer - left_pointer + 1


if __name__ == '__main__':
    il = [
        'ca',
        'cabaabac',
        'aabccabba',
        # 'aa',
    ]

    s = Solution()

    for item in il:
        pprint(s.minimumLength(item))
    pass
