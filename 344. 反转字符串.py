# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.19 21:49
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。

 

示例 1：

输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
示例 2：

输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnhbqj/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def reverseString(s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    n = len(s)
    # 对称交换
    # for i in range(int(n/2)):
    #     if s[i] != s[n-1-i]:
    #         s[i], s[n-1-i] = s[n-1-i], s[i]

    # 双指针
    start = 0
    end = n - 1
    while start < end:
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    pprint(s)
    reverseString(s)
    pprint(s)
    pass
