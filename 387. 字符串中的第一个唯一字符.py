# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.20 18:53
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2
 

提示：你可以假定该字符串只包含小写字母。

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xn5z8r/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def firstUniqChar(s: str) -> int:
    # 利用字典记录键值对,python3.6之后字典有序
    # n = len(s)
    #
    # temp_dict = {}
    #
    # for i in range(n):
    #     if s[i] in temp_dict:
    #         temp_dict[s[i]] += 1
    #     else:
    #         temp_dict[s[i]] = 1
    #
    # for key in temp_dict:
    #     if temp_dict[key] == 1:
    #         return s.index(key)
    #
    # return -1

    # 利用内置函数
    n = len(s)
    for i in range(n):
        if s.index(s[i]) == s.rindex(s[i]):
            return i
    return -1


def random_lowercase_letter() -> str:
    return chr(random.randint(97, 122))


if __name__ == '__main__':
    n = random.randint(5, 10)
    s = ""
    for i in range(n):
        s += random_lowercase_letter()
    pprint(s)
    index = firstUniqChar(s)
    pprint(index)
    pprint(s[index])

    pass
