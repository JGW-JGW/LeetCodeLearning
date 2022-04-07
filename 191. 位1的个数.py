# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-07 21:01
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为汉明重量）。

提示：

请注意，在某些语言（如 Java）中，没有无符号整数类型。在这种情况下，输入和输出都将被指定为有符号整数类型，并且不应影响您的实现，因为无论整数是有符号的还是无符号的，其内部的二进制表示形式都是相同的。
在 Java 中，编译器使用二进制补码记法来表示有符号整数。因此，在上面的 示例 3 中，输入表示有符号整数 -3。

提示：

输入必须是长度为 32 的 二进制串 。
 

进阶：

如果多次调用这个函数，你将如何优化你的算法？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-1-bits
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def hammingWeight(n: int) -> int:
        ans = 0
        while n != 0:
            if n & 1 == 1:
                ans += 1
            n >>= 1

        return ans


if __name__ == '__main__':
    il = [
        0b00000000000000000000000000001011,
        0b00000000000000000000000010000000,
        0b11111111111111111111111111111101,
    ]
    s = Solution()
    for n in il:
        pprint(s.hammingWeight(n))
    pass
