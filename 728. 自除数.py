# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-31 21:08
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
from collections import Counter

"""
自除数 是指可以被它包含的每一位数整除的数。

例如，128 是一个 自除数 ，因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。
自除数 不允许包含 0 。

给定两个整数 left 和 right ，返回一个列表，列表的元素是范围 [left, right] 内所有的 自除数

提示：

1 <= left <= right <= 10^4

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/self-dividing-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
含有 1，无需验证
含有 2，个位必须是 2 4 6 8，一定是偶数
含有 3，各位数之和必须是 3 的倍数
含有 4，个位和十位所组成的两位数能被 4 整除，一定是偶数
含有 5，个位只能是 5，一定是奇数
含有 6，各位数之和必须是 3 的倍数，一定是偶数
含有 7，截断个位数，余下的数 减去 个位数的2倍，若差为 7 的倍数，则可以被7整除。该过程可以重复进行。
含有 8，一个数的后三位若能被 8 整除，则该数一定能被 8 整除，一定是偶数
含有 9，各位数之和必须是 9 的倍数
"""


class Solution:
    @staticmethod
    def is_self_divided(num: int) -> bool:
        counter = Counter()
        digit_list = []
        origin = num
        while num > 0:
            digit = num % 10
            digit_list.append(digit)
            counter[digit] += 1
            num = num // 10

        if 0 in counter:
            return False

        if 7 in counter and origin % 7 != 0:
            return False

        n = len(digit_list)
        sum_of_digits = sum(digit_list)

        if 5 in counter:
            if digit_list[0] != 5 or 2 in counter or 4 in counter or 6 in counter or 8 in counter:
                return False

        if 2 in counter:
            if digit_list[0] & 1 == 1:
                return False

        if 3 in counter:
            if sum_of_digits % 3 != 0:
                return False

        if 4 in counter:
            if n > 1 and (10 * digit_list[1] + digit_list[0]) % 4 != 0:
                return False
            if n == 1 and digit_list[0] != 4 and digit_list[0] != 8:
                return False

        if 6 in counter:
            if sum_of_digits % 3 != 0 or digit_list[0] & 1 == 1:
                return False

        if 8 in counter:
            if n > 2:
                if (100 * digit_list[2] + 10 * digit_list[1] + digit_list[0]) % 8 != 0:
                    return False
            elif origin % 8 != 0:
                return False

        if 9 in counter:
            if sum_of_digits % 9 != 0:
                return False

        return True

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right + 1):
            if self.is_self_divided(i):
                res.append(i)

        return res


if __name__ == '__main__':
    pass
