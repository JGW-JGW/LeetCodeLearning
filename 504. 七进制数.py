# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-07 22:43
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""

"""


class Solution:
    @staticmethod
    def convertToBase7(num: int) -> str:
        char_list = []
        abs_value = abs(num)
        while abs_value >= 7:
            abs_value, mod = divmod(abs_value, 7)
            char_list.append(str(mod))
        char_list.append(str(abs_value))
        if num < 0:
            char_list.append('-')

        return "".join(reversed(char_list))


if __name__ == '__main__':
    s = Solution()

    il = [
        100,
        99,
        -7
    ]

    for item in il:
        pprint(s.convertToBase7(item))

    pass
