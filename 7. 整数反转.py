# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.19 21:59
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

假设环境不允许存储 64 位整数（有符号或无符号）。
 

示例 1：

输入：x = 123
输出：321
示例 2：

输入：x = -123
输出：-321
示例 3：

输入：x = 120
输出：21
示例 4：

输入：x = 0
输出：0
 

提示：

-231 <= x <= 231 - 1

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnx13t/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def reverse(x: int) -> int:
    # if x != 0:
    #     x_abs = abs(x)
    #     x_sign = int(x / x_abs)
    #     n = len(str(x_abs))
    #     result = 0
    #     for i in range(n - 1, -1, -1):
    #         result += int(x_abs / (10 ** i)) * (10 ** (n - 1 - i))
    #         if x_sign > 0 and result > 2 ** 31 - 1:
    #             return 0
    #         elif x_sign < 0 and result > 2 ** 31:
    #             return 0
    #         x_abs -= int(x_abs / (10 ** i)) * (10 ** i)
    #     return x_sign * result
    # else:
    #     return 0
    num = int(str(abs(x))[::-1])
    s = -num if x < 0 else num
    return s if -2 ** 31 <= s <= 2 ** 31 - 1 else 0


if __name__ == '__main__':
    x = random.randint(-2 ** 31, 2 ** 31 - 1)
    pprint(-2 ** 31)
    pprint(2 ** 31 - 1)
    pprint(x)
    pprint(reverse(x))
    pass
