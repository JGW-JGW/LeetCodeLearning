# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-03 19:18
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

"""


class Solution:
    @staticmethod
    def largestMultipleOfThree(digits: List[int]) -> str:
        counter = Counter(digits)
        sum_digits = 0
        for digit in [8, 7, 5, 4, 2, 1]:
            if digit in counter:
                sum_digits += digit * counter[digit]

        result = ''
        mod = sum_digits % 3
        if mod == 0:
            for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                if digit in counter:
                    result += str(digit) * counter[digit]
            if result == '':
                return '0'
            elif 0 in counter:
                result += '0' * counter[0]
                return result

        elif mod == 1:  # 各位数字之和除以3余1，此时-1或-4或-7或-2-5或-2-8或-5-8
            for i in [1, 4, 7]:
                if i in counter:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]
                    for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                        if digit in counter:
                            result += str(digit) * counter[digit]

                    if result == '':
                        return '0' if 0 in counter else ''
                    else:
                        if 0 in counter:
                            result += '0' * counter[0]
                        return result

            if 2 in counter and counter[2] > 1:
                counter[2] -= 2
                if counter[2] == 0:
                    del counter[2]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

            if 2 in counter and 5 in counter:
                for i in [2, 5]:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

            if 5 in counter and counter[5] > 1:
                counter[5] -= 2
                if counter[5] == 0:
                    del counter[5]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

            if 2 in counter and 8 in counter:
                for i in [2, 8]:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

            if 5 in counter and 8 in counter:
                for i in [5, 8]:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

            if 8 in counter and counter[8] > 1:
                counter[8] -= 2
                if counter[8] == 0:
                    del counter[8]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result



        else:  # 余数为2
            for i in [2, 5, 8]:
                if i in counter:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]
                    for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                        if digit in counter:
                            result += str(digit) * counter[digit]
                    if result == '':
                        return '0' if 0 in counter else ''
                    else:
                        if 0 in counter:
                            result += '0' * counter[0]
                        return result

            if 1 in counter and counter[1] > 1:
                counter[1] -= 2
                if counter[1] == 0:
                    del counter[1]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

            if 1 in counter and 4 in counter:
                for i in [1, 4]:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

            if 4 in counter and counter[4] > 1:
                counter[4] -= 2
                if counter[4] == 0:
                    del counter[4]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

            if 1 in counter and 7 in counter:
                for i in [1, 7]:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

            if 4 in counter and 7 in counter:
                for i in [5, 8]:
                    counter[i] -= 1
                    if counter[i] == 0:
                        del counter[i]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

            if 7 in counter and counter[7] > 1:
                counter[7] -= 2
                if counter[7] == 0:
                    del counter[7]

                for digit in [9, 8, 7, 6, 5, 4, 3, 2, 1]:
                    if digit in counter:
                        result += str(digit) * counter[digit]

                if result == '':
                    return '0' if 0 in counter else ''
                else:
                    if 0 in counter:
                        result += '0' * counter[0]
                    return result

        return result


class Solution:
    @staticmethod
    def largestMultipleOfThree(digits: List[int]) -> str:
        cnt, modulo = [0] * 10, [0] * 3
        s = 0
        for digit in digits:
            cnt[digit] += 1
            modulo[digit % 3] += 1
            s += digit

        remove_mod, rest = 0, 0
        if s % 3 == 1:
            remove_mod, rest = (1, 1) if modulo[1] >= 1 else (2, 2)
        elif s % 3 == 2:
            remove_mod, rest = (2, 1) if modulo[2] >= 1 else (1, 2)

        ans = ""
        for i in range(0, 10):
            for j in range(cnt[i]):
                if rest > 0 and remove_mod == i % 3:
                    rest -= 1
                else:
                    ans += str(i)
        if len(ans) > 0 and ans[-1] == "0":
            ans = "0"
        return ans[::-1]


if __name__ == '__main__':
    solution = Solution()
    input_list = [
        # [8, 1, 9],
        # [8, 6, 7, 1, 0],
        # [1],
        # [0, 0, 0, 0, 0],
        [9, 8, 6, 8, 6],
    ]
    for item in input_list:
        pprint(solution.largestMultipleOfThree(item))
    pass
