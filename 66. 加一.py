# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.11 17:11
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

 

示例 1：

输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123。
示例 2：

输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321。
示例 3：

输入：digits = [0]
输出：[1]
 

提示：

1 <= digits.length <= 100
0 <= digits[i] <= 9

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2cv1c/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def plusOne(digits: List[int]) -> List[int]:
    # 从个位开始找连续的9的个数
    # 如果找到1个9，倒数第2位加1，倒数第1位变0
    # 如果找到k个9，倒数第k+1位加1，倒数第1位至第k位变0
    n = len(digits)
    i = n - 1
    counter = 0
    while digits[i] == 9:
        digits[i] = 0
        counter += 1
        i -= 1
    if counter < n:
        digits[n - 1 - counter] += 1
    else:
        digits.insert(0, 1)

    return digits


if __name__ == '__main__':
    value_min = 1
    value_max = 9
    len_min = 3
    len_max = 9
    digits = [random.randint(value_min, value_max) for i in range(random.randint(len_min, len_max))]
    digits = [9, 9, 9, 9, 9, 9, 9]
    pprint(digits)
    pprint(plusOne(digits))
