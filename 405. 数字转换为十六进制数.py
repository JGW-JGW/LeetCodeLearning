# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-11 16:01
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个整数，编写一个算法将这个数转换为十六进制数。对于负整数，我们通常使用 补码运算 方法。

注意:

十六进制中所有字母(a-f)都必须是小写。
十六进制字符串中不能包含多余的前导零。如果要转化的数为0，那么以单个字符'0'来表示；对于其他情况，十六进制字符串中的第一个字符将不会是0字符。 
给定的数确保在32位有符号整数范围内。
不能使用任何由库提供的将数字直接转换或格式化为十六进制的方法。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-a-number-to-hexadecimal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def num2str(num: int) -> str:
        if 0 <= num <= 9:
            return str(num)
        else:
            return chr(num + 87)

    def toHex(self, num: int) -> str:
        if num > 0:
            str_list = []
            while num != 0:
                str_list.append(self.num2str(num & 0b1111))
                num = num >> 4

            str_list.reverse()

            return ''.join(str_list)

        elif num < 0:
            num &= 0xffffffff
            str_list = []
            while num != 0:
                str_list.append(self.num2str(num & 0b1111))
                num = num >> 4

            str_list.reverse()

            return ''.join(str_list)

        else:
            return '0'


if __name__ == '__main__':
    il = [
        26,
        -1
    ]
    s = Solution()
    for num in il:
        pprint(s.toHex(num))
    pass
