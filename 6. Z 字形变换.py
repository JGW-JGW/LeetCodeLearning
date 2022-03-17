# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-01 18:09
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。

比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：

P   A   H   N
A P L S I I G
Y   I   R
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："PAHNAPLSIIGYIR"。

请你实现这个将字符串进行指定行数变换的函数：

string convert(string s, int numRows);

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/zigzag-conversion
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# noinspection PyPep8Naming
class Solution:
    @staticmethod
    def convert(s: str, numRows: int) -> str:
        n = len(s)

        if n <= numRows or numRows == 1:
            return s

        if numRows == 2:
            return s[0:n:2] + s[1:n:2]

        result = ''
        for row in range(0, numRows):
            row_str = ''
            max_diff = 2 * numRows - 2
            if row == 0 or row == numRows - 1:
                row_str += s[row:n:max_diff]
            else:  # 1 <= row <= numRows - 2
                diff_back = 2 * row
                diff_front = max_diff - diff_back
                pos = row
                row_str += s[pos]
                while True:
                    pos += diff_front
                    if pos >= n:
                        break
                    row_str += s[pos]
                    pos += diff_back
                    if pos >= n:
                        break
                    row_str += s[pos]
            result += row_str

        return result


if __name__ == '__main__':
    solution = Solution()
    input_list = [
        # ('PAYPALISHIRING', 3),
        # ('PAYPALISHIRING', 4),
        # ('A', 1),
        ('A', 3),
    ]
    for item in input_list:
        pprint(solution.convert(item[0], item[1]))
    pass
