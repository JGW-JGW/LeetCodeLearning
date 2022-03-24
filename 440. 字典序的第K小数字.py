# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-23 20:25
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
from math import log10
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
from collections import defaultdict

"""
给定整数 n 和 k，返回  [1, n] 中字典序第 k 小的数字。

提示:

1 <= k <= n <= 10^9
"""

"""
先来一波转字符串暴力法，写法简单，效率肯定很低
"""


class Solution:
    @staticmethod
    def findKthNumber(n: int, k: int) -> int:
        int_list = list(range(1, n + 1))
        str_list = [str(item) for item in int_list]

        return int(sorted(str_list)[k - 1])


"""
上面那个方法，超时。

换个思路。

字典序，只有 9 种开头的数字：
1 ~ 9

各开头的数字的位数的可能值：
    1: 1 ~ 10
2 ~ 9: 1 ~ 9

"""


class Solution1:
    @staticmethod
    def calc_digits_of_int(num: int) -> int:
        return int(log10(num)) + 1

    def findKthNumber(self, n: int, k: int) -> int:
        count_of_digit = defaultdict(int)
        cumulative_count_of_digit = defaultdict(int)
        list_of_digit = defaultdict(list)
        for num in range(1, n + 1):
            digit = self.calc_digits_of_int(num)
            count_of_digit[digit] += 1
            for i in range(digit, 11):
                cumulative_count_of_digit[i] += 1
            list_of_digit[digit].append(num)

        for i in range(1, 11):
            if cumulative_count_of_digit[i - 1] < k <= cumulative_count_of_digit[i]:
                return list_of_digit[i][k - cumulative_count_of_digit[i - 1] - 1]


"""
以上方法，结果有问题，而且更慢，铁定超时。

看来只能尝试数学解法。

当 1 <= n <= 9 时
直接返回 k

当 10 <= n <= 19 时
数组为 [1, 10, ..., n, 2, 3, 4, 5, 6, 7, 8, 9]，数组长度为 n
以 1 开头的子数组的长度为 1 + n - 10 + 1 = n - 8

当 20 <= n <= 29 时
数组为 [1, 10, ..., 19, 2, 20, ..., n, 3, 4, 5, 6, 7, 8, 9]，数组长度为 n
以 1 开头的子数组的长度为 10
以 2 开头的子数组的长度为 1 + n - 20 + 1 = n - 18

当 X0 <= n <= X9 时 (X = 1 ~ 9)
以 1 开头的子数组的长度为 X > 1 ? (10 ^ (n的位数 - 1)) : n - 1 * (10 ^ (n的位数 - 1)) + 2
以 Y 开头的子数组的长度为 X > Y ? (10 ^ (n的位数 - 1)) : (X < Y ? 1 : 1 + n - Y * (10 ^ (n的位数 - 1)) + 1)

当 100 <= n <= 109 时
数组为 [1, 10, 100, ..., n, 11, ..., 19, 2, 20, ..., 29, ......, 9, 90, ..., 99]
以 1 开头的子数组的长度为 1 + 10 + n - 100 + 1
以 2 ~ 9 开头的子数组的长度为 1 + 10

当 200 <= n <= 299 时
数组为 [1, 11, ..., 19, 100, ..., 199, 2, 20, ..., 29, 200, ..., n, 3, ..., 39, 4, ..., 49, ......, 9, ..., 99]
以 1 开头的子数组的长度为 1 + 10 + 100
以 2 开头的子数组的长度为 1 + 10 + n - 200 + 1
以 3 - 9 开头的子数组的长度为 1 + 10

当 X00 <= n <= X99 时
以 Y 开头的子数组的长度为 X == Y ? (1 + 10 + n - X * 10^(n的位数 - 1) + 1) : (X > Y ? (1 + 10 + 10^(n的位数 - 1)) : (1 + 10))

当 X * 10^N <= n <= X * 10^N + 10^N - 1 = (X + 1) * 10^N - 1 (N 为 n的位数 - 1)
以 Y 开头的子数组的长度为 X == Y ? (1 + 10 + ... + 10^(N-1) + n - X * 10^N + 1) : (X > Y ? (1 + 10 + ... + 10^N) : (1 + 10 + ... + 10^(N-1)))

N = n的位数 - 1
X = n // 10 ^ N

由此可以计算获得 1 ~ 9 开头的数字的数量

之后可以获得 k 落在哪个区间

不妨设 k 落在以 Y 开头的数字的区间内

假设以 Y 开头的数字之前的所有数字的个数为 count_of_above

则需要寻找以 Y 开头的数字当中，第 k - count_of_above 个数字

记 order = k - count_of_above

若 order == 1，则：
要找的数字一定为 Y

若 1 < order <= 1 + 10，则：
要找的数字一定为 Y * 10 + order - 1 - 1

若 1 + 10 < order <= 1 + 10 + 100，则：
要找的数字一定为 Y * 100 + order - (1 + 10) - 1

若 1 + 10 + 100 < order <= 1 + 10 + 100 + 1000，则：
要找的数字一定为 Y * 1000 + order - (1 + 10 + 100) - 1

若 1 + 10 + ... + 10^(N-1) < order <= 1 + 10 + ... + 10^N，则：
要找的数字一定为 Y * 10^N + order - (1 + 10 + ... + 10^(N-1)) - 1
"""


class Solution2:
    @staticmethod
    def calc_digits_of_int(num: int) -> int:
        return int(log10(num)) + 1

    @staticmethod
    def calc_sum_of_power(digit: int) -> int:
        """
        计算由 digit 位数的 1 构成的数字，比如，digit 为 2 时，返回 11
        :param digit: 位数，显然 digit >= 1
        :return: digit 位数的 1
        """
        s = 0

        for i in range(digit):
            s += 10 ** i

        return s

    # noinspection PyPep8Naming
    def findKthNumber(self, n: int, k: int) -> int:
        # 获取 n的位数 - 1
        N = self.calc_digits_of_int(n) - 1

        # 获取 n的最高位数字
        X = n // (10 ** N)

        # 获取以 1 ~ 9 开头的数字的个数
        count_of_begin_with_Y = [0 for _ in range(10)]

        """
        当 X * 10^N <= n <= X * 10^N + 10^N - 1 = (X + 1) * 10^N - 1 (N 为 n的位数 - 1)
        以 Y 开头的子数组的长度为 X == Y ? (1 + 10 + ... + 10^(N-1) + n - X * 10^N + 1) : (X > Y ? (1 + 10 + ... + 10^N) : (1 + 10 + ... + 10^(N-1)))
        """
        for Y in range(1, 10):
            if X > Y:
                count_of_begin_with_Y[Y] = self.calc_sum_of_power(N + 1)

            elif X < Y:
                count_of_begin_with_Y[Y] = self.calc_sum_of_power(N)

            else:  # X == Y
                count_of_begin_with_Y[Y] = self.calc_sum_of_power(N)
                count_of_begin_with_Y[Y] += n - X * (10 ** N) + 1

        # 获取 k 落在哪个数字开头的区间内
        Y = 0
        k_copy = k
        for y in range(1, 10):
            k_copy -= count_of_begin_with_Y[y]
            if k_copy <= 0:
                Y = y
                break

        # 获取 order
        order = k
        for y in range(1, Y):
            order -= count_of_begin_with_Y[y]

        """
        若 order == 1，则：
        要找的数字一定为 Y
        
        若 1 + 10 + ... + 10^(N_order-1) < order <= 1 + 10 + ... + 10^N_order，则：
        要找的数字一定为 Y * 10^N_order + order - (1 + 10 + ... + 10^(N_order-1)) - 1 
        """
        if order == 1:
            return Y
        else:
            N_order = 1
            while order <= self.calc_sum_of_power(N_order) or order > self.calc_sum_of_power(N_order + 1):
                N_order += 1

            return Y * (10 ** N_order) + order - self.calc_sum_of_power(N_order) - 1

        pass


"""
以上方法，想错了一件事，优先考虑了位数而非字典序，比如把 100 排在了 19 的后面

而 100 ~  109 的位置应该在 10 后面

这样一来准备参考一下标答，好像是通过模拟字典树归纳出规律……2022-03-24继续

[2022-03-24]

看了一下参考答案，发现也就那么回事，还是再静下心来自己琢磨一下吧

当 1 <= n <= 9 时
直接返回 k

当 10 <= n <= 19 时
数组为 [1, 10, ..., n, 2, 3, 4, 5, 6, 7, 8, 9]，数组长度为 n
以 1 开头的子数组长度为 1 + n - 1*10 + 1

当 20 <= n <= 29 时
数组为 [1, 10, ..., 19, 2, 20, ..., n, 3, 4, 5, 6, 7, 8, 9]，数组长度为 n
以 1 开头的子数组长度为 1 + 1*10
以 2 开头的子数组长度为 1 + n - 2*10 + 1

当 30 <= n <= 39 时
数组为 [1, 10, ..., 19, 2, 20, ..., 29, 3, 30, ..., n, 4, 5, 6, 7, 8, 9]
以 1 开头的子数组长度为 1 + 1*10
以 2 开头的子数组长度为 1 + 1*10
以 3 开头的子数组长度为 1 + n - 3*10 + 1

归纳：
当 X0 <= n <= X9 时 (X = [1-9])
以 Y 开头的子数组的长度为
若 X > Y，则为 1 + 10
若 X = Y，则为 1 + n - Y*10 + 1
若 X < Y，则为 1

当 100 <= n <= 109 时
数组为 [
1, 10, 100, ..., n, 11, ..., 19,
2, 20, ..., 29,
3, 30, ..., 39,
..............,
9, 90, ..., 99
]
以 1 开头的子数组的长度为 1 + 10 + n - 100 + 1
= 1 + 10 - n//10*10 + 1
以 2 ~ 9 开头的子数组的长度为 1 + 10

当 110 <= n <= 119 时
数组为 [
1, 10, 100, ..., 109, 11, 110, ..., n, 12, 13, ..., 19,
2, 20, ..., 29,
3, 30, ..., 39,
..............,
9, 90, ..., 99
]
以 1 开头的子数组的长度为 1 + 10 + 10 + n - 110 + 1
= 1 + 10 - n//10*10 + n + 1
以 2 ~ 9 开头的子数组的长度为 1 + 10

归纳：
当 100 <= n <= 199 时
以 1 开头的子数组长度为 1 + 10 - n//10*10 + 1
以 2 ~ 9 开头的子数组的长度为 1 + 10

当 200 <= n <= 209 时
数组为 [
1, 10, ..., 109, 11, ..., 119, 12, ..., 129, 13, ..., 139, 14, ......, 19, ..., 199,
2, 20, 200, ..., 209, 21, ..., 29,
3, 30, ..., 39,
..............,
9, 90, ..., 99
]
以 1 开头的子数组长度为 1 + 10 + 100
以 2 开头的子数组长度为 1 + 10 + n - 200 + 1
= 1 + 10 - n//10*10 + n + 1
以 3 ~ 9 开头的子数组长度为 1 + 10

归纳：
当 100 <= n <= 999 时
以 Y 开头的子数组长度为
若 Y < n//100，则为 1 + 10 + 100
若 Y = n//100，则为 1 + 10 + n - n//10*10 + 1
若 Y > n//100，则为 1 + 10

归纳：
当 X * 10^N <= n <= X * 10^N + 10^N - 1 = (X + 1) * 10^N - 1 (N 为 n的位数 - 1)
以 Y 开头的子数组的长度为 X == Y ? (1 + 10 + ... + 10^(N-1) + n - X * 10^N + 1) : (X > Y ? (1 + 10 + ... + 10^N) : (1 + 10 + ... + 10^(N-1)))

N = n的位数 - 1
X = n // 10 ^ N

由此可以计算获得 1 ~ 9 开头的数字的数量

之后可以获得 k 落在哪个区间

不妨设 k 落在以 Y 开头的数字的区间内

假设以 Y 开头的数字之前的所有数字的个数为 count_of_above

则需要寻找以 Y 开头的数字当中，第 k - count_of_above 个数字

记 order = k - count_of_above

抄作业…………………………………………………………………………
"""


class Solution3:
    # 计算以数字 i 开头，且不超过最大数字 n 的数字个数
    @staticmethod
    def get_count(i: int, n: int) -> int:
        count = 0
        # 区间起点设为 a 和 b
        a = i
        b = i + 1
        while a <= n:
            count += min(n + 1, b) - a
            a *= 10
            b *= 10

        return count

    # noinspection PyPep8Naming
    def findKthNumber(self, n: int, k: int) -> int:
        # i 表示从以 i 开头的数字开始搜索
        i = 1
        # p 为初始位置
        p = 1
        while p < k:
            count = self.get_count(i, n)
            if p + count > k:
                i *= 10
                p += 1
            else:
                i += 1
                p += count

        return i


if __name__ == '__main__':
    s = Solution3()

    il = [
        # (13, 2),
        # (101, 14),
        # (1, 1),
        (7747794, 5857460),  # 6271710
    ]

    for t in il:
        pprint(s.findKthNumber(n=t[0], k=t[1]))

    pass
