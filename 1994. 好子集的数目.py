# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-02-22 18:20
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
1 <= nums.length <= 10^5
1 <= nums[i] <= 30

special:
1

ignore:
4 8 9 12 16 18 20 24 25 27 28

prime_list = [2, 3, 5 ,7, 11, 13, 17, 19, 23, 29]

combination of prime:
30 = 2 * 3 * 5
26 = 2 * 13
22 = 2 * 11
21 = 3 * 7
15 = 3 * 5
14 = 2 * 7
10 = 2 * 5
 6 = 2 * 3

choose 30

"""


class Solution:
    def __init__(self):
        self.count_list = None

    @staticmethod
    def get_remain_prime_list(*args) -> List[int]:
        args_len = len(args)
        if args_len == 0:
            return [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

        elif args_len == 1:
            n = args[0]
            if n == 30:
                return [7, 11, 13, 17, 19, 23, 29]
            elif n == 26:
                return [3, 5, 7, 11, 17, 19, 23, 29]
            elif n == 22:
                return [3, 5, 7, 13, 17, 19, 23, 29]
            elif n == 21:
                return [2, 5, 11, 13, 17, 19, 23, 29]
            elif n == 15:
                return [2, 7, 11, 13, 17, 19, 23, 29]
            elif n == 14:
                return [3, 5, 11, 13, 17, 19, 23, 29]
            elif n == 10:
                return [3, 7, 11, 13, 17, 19, 23, 29]
            elif n == 6:
                return [5, 7, 11, 13, 17, 19, 23, 29]
            else:
                raise ValueError("unsupported value: n = {}".format(n))

        elif args_len == 2:
            if args == (26, 21):
                return [5, 11, 17, 19, 23, 29]
            elif args == (26, 15):
                return [7, 11, 17, 19, 23, 29]
            elif args == (22, 21):
                return [5, 13, 17, 19, 23, 29]
            elif args == (22, 15):
                return [7, 13, 17, 19, 23, 29]
            elif args == (21, 10):
                return [11, 13, 17, 19, 23, 29]
            elif args == (15, 14):
                return [11, 13, 17, 19, 23, 29]
            else:
                raise ValueError("unsupported value: args = {}".format(args))

        else:
            raise ValueError("args_len = {}, should be less than 3.".format(args_len))

    def count(self, n: int) -> int:
        return self.count_list[n - 1]

    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        self.count_list = [0 for _ in range(30)]
        for item in nums:
            self.count_list[item - 1] += 1

        result = 0
        factor_1 = 2 ** self.count(1)

        for k in [30, 26, 22, 21, 15, 14, 10, 6]:
            temp = self.count(k)
            if temp > 0:
                for prime in self.get_remain_prime_list(k):
                    temp *= (self.count(prime) + 1)
                result += temp

        for t in [(26, 21), (26, 15), (22, 21), (22, 15), (21, 10), (15, 14)]:
            temp = self.count(t[0]) * self.count(t[1])
            if temp > 0:
                for prime in self.get_remain_prime_list(t[0], t[1]):
                    temp *= (self.count(prime) + 1)
                result += temp

        temp = 1
        for prime in self.get_remain_prime_list():
            temp *= (self.count(prime) + 1)
        temp -= 1

        result += temp

        return (result * factor_1) % int(1e9 + 7)


if __name__ == '__main__':
    solution = Solution()
    input_list = [
        [3, 14, 14, 3, 23, 23, 30, 2, 6, 26, 17, 5, 23, 6, 2, 30, 21, 19, 1, 23, 22, 26, 17,
         5, 15, 22, 2, 15, 21]
    ]
    for item in input_list:
        pprint(solution.numberOfGoodSubsets(item))
