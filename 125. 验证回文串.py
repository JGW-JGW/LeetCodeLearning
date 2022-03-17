# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.20 21:09
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

 

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
解释："amanaplanacanalpanama" 是回文串
示例 2:

输入: "race a car"
输出: false
解释："raceacar" 不是回文串
 

提示：

1 <= s.length <= 2 * 105
字符串 s 由 ASCII 字符组成

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xne8id/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def isPalindrome(s: str) -> bool:
    # 双指针
    n = len(s)
    s_lower = s.lower()
    i = 0
    j = n - 1
    while i < j:
        if s_lower[i].isalnum() and s_lower[j].isalnum():
            if s_lower[i] != s_lower[j]:
                return False
            else:
                i += 1
                j -= 1
        elif s_lower[i].isalnum() and not s_lower[j].isalnum():
            j -= 1
        elif not s_lower[i].isalnum() and s_lower[j].isalnum():
            i += 1
        else:
            i += 1
            j -= 1
    return True


if __name__ == '__main__':
    s = "0P"
    print(isPalindrome(s))
    pass
