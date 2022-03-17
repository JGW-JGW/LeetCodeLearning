# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.22 17:28
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

 

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

 

示例 1：

输入：haystack = "hello", needle = "ll"
输出：2
示例 2：

输入：haystack = "aaaaa", needle = "bba"
输出：-1
示例 3：

输入：haystack = "", needle = ""
输出：0
 

提示：

0 <= haystack.length, needle.length <= 5 * 104
haystack 和 needle 仅由小写英文字符组成

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnr003/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# Sunday算法被某极端测试样例搞超时了，所以老老实实写KMP算法，简直草泥马
# def strStr(haystack: str, needle: str) -> int:
#     n_haystack = len(haystack)
#     n_needle = len(needle)
#
#     if n_needle > n_haystack:
#         return -1
#
#     if n_haystack > 0:
#         if 0 < n_needle <= n_haystack:
#             offset = {}
#
#             for i in range(n_needle):
#                 offset[needle[i]] = n_needle - i
#             i = 0
#             while i <= n_haystack - n_needle:
#                 j = 0
#                 while haystack[i + j] == needle[j]:
#                     j += 1
#                     if j == n_needle:
#                         return i
#
#                 if i + n_needle == n_haystack:
#                     return -1
#
#                 if haystack[i + n_needle] in offset:
#                     i += offset[haystack[i + n_needle]]
#                 else:
#                     i += n_needle + 1
#
#             return -1
#
#         else:  # n_needle == 0
#             return 0
#     elif n_needle == 0:  # n_haystack == 0 and n_needle == 0
#         return 0

def get_next(s: str) -> list:
    n = len(s)
    output = [0 for i in range(n)]
    i, k = 0, -1
    output[0] = -1
    while i < n - 1:
        if k == -1 or s[i] == s[k]:
            i += 1
            k += 1
            if s[i] == s[k]:
                output[i] = output[k]
            else:
                output[i] = k
        else:
            k = output[k]
    return output


def strStr(haystack: str, needle: str) -> int:
    n_haystack = len(haystack)
    n_needle = len(needle)

    if n_needle > n_haystack:
        return -1

    if n_haystack > 0:
        if 0 < n_needle <= n_haystack:
            next = get_next(needle)
            i = 0
            j = 0
            while i < n_haystack and j < n_needle:
                if j == -1 or haystack[i] == needle[j]:
                    i += 1
                    j += 1
                else:
                    j = next[j]

            if j >= n_needle:
                return i - n_needle
            else:
                return -1

        else:  # n_needle == 0
            return 0
    elif n_needle == 0:  # n_haystack == 0 and n_needle == 0
        return 0


if __name__ == '__main__':
    # ASCII: a - z: 97 - 122
    n_haystack = random.randint(1, 5000)
    n_needle = random.randint(1, 3)

    haystack = ''
    needle = ''

    for i in range(n_haystack):
        haystack += chr(random.randint(97, 122))

    for j in range(n_needle):
        needle += chr(random.randint(97, 122))

    # haystack = 'kvgvgvgsabzaxcbtkmpjzjez'
    # needle = 'ez'
    # haystack = "mississippi"
    # needle = "issip"
    # haystack = 'a'
    # needle = 'a'
    # haystack = 'aaaaa'
    # needle = 'bba'
    # haystack = 'abc'
    # needle = 'c'
    # haystack = "mississippi"
    # needle = "sippj"

    index = strStr(haystack, needle)
    print('haystack:\t{}'.format(haystack))
    print('needle:\t\t{}'.format(needle))
    pprint('index = {}'.format(index))
    result = ''
    for i in range(index, index + len(needle)):
        result += haystack[i]
    if index >= 0 and needle != '':
        pprint('result = {}'.format(result))

    pass
