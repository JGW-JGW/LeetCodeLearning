# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.20 20:05
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。

 

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false
 

提示:

1 <= s.length, t.length <= 5 * 104
s 和 t 仅包含小写字母
 

进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn96us/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def isAnagram(s: str, t: str) -> bool:
    # 用两个字典记录出现次数，最后再判断是否键都一样且值都一样
    # n_s = len(s)
    # n_t = len(t)
    # if n_s == n_t:
    #     dict_s = {}
    #     dict_t = {}
    #     for i in range(n_s):
    #         if s[i] in dict_s:
    #             dict_s[s[i]] += 1
    #         else:
    #             dict_s[s[i]] = 1
    #
    #         if t[i] in dict_t:
    #             dict_t[t[i]] += 1
    #         else:
    #             dict_t[t[i]] = 1
    #
    #     for key in dict_s:
    #         if key not in dict_t or dict_s[key] != dict_t[key]:
    #             return False
    #
    #     return True
    # else:
    #     return False

    # 用一个字典记录出现次数，遍历另一个字符串，将数值往下减
    # n_s = len(s)
    # n_t = len(t)
    # dict_s = {}
    # for i in range(n_s):
    #     if s[i] in dict_s:
    #         dict_s[s[i]] += 1
    #     else:
    #         dict_s[s[i]] = 1
    #
    # for i in range(n_t):
    #     if t[i] not in dict_s:
    #         return False
    #     else:
    #         dict_s[t[i]] -= 1
    #         if dict_s[t[i]] < 0:
    #             return False
    #
    # for key in dict_s:
    #     if dict_s[key] > 0:
    #         return False
    #
    # return True

    # 先排序再遍历
    # n_s = len(s)
    # n_t = len(t)
    # list_s = list(s)
    # list_t = list(t)
    # if n_s == n_t:
    #     list_s.sort()
    #     list_t.sort()
    #     for i in range(n_s):
    #         if list_s[i] != list_t[i]:
    #             return False
    #     return True
    # else:
    #     return False

    # 简化为一行，大神真牛逼
    return sorted(s) == sorted(t)


if __name__ == '__main__':
    s = 'babdac'
    t = 'caabb'
    pprint(isAnagram(s, t))
    pass
