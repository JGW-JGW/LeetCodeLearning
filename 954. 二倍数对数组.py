# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-01 20:51
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
给定一个长度为偶数的整数数组 arr，只有对 arr 进行重组后可以满足 “对于每个 0 <= i < len(arr) / 2，都有 arr[2 * i + 1] = 2 * arr[2 * i]” 时，返回 true；否则，返回 false。

提示：

0 <= arr.length <= 3 * 10^4
arr.length 是偶数
-10^5 <= arr[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/array-of-doubled-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def canReorderDoubled(arr: List[int]) -> bool:
        counter = Counter(arr)
        sorted_keys = sorted(counter.keys())

        if 0 in counter and counter[0] & 1 == 1:
            return False

        for key in sorted_keys:
            if key in counter.keys():
                if key < 0:
                    # 绝对值最大的负数是奇数，则肯定是不行的
                    if key & 1 == 1:
                        return False

                    # 到这里说明绝对值最大的负数是偶数，可获得期望的键
                    expected_key = key // 2

                    # 如果没找到期望的键，或者期望的键数量不够，则肯定不行
                    if expected_key not in counter.keys() or counter[expected_key] < counter[key]:
                        return False

                    # 如果期望的键的数量正好够，则删掉这个期望的键
                    if counter[expected_key] == counter[key]:
                        del counter[expected_key]
                    else:  # 数量比key数量多，则干掉key数量的expected_key
                        counter[expected_key] -= counter[key]

                    # key被用完了，干掉
                    del counter[key]
                else:
                    break

        sorted_keys.reverse()
        for key in sorted_keys:
            if key in counter.keys():
                if key > 0:
                    # 绝对值最大的正数是奇数，则肯定是不行的
                    if key & 1 == 1:
                        return False

                    # 到这里说明绝对值最大的正数是偶数，可获得期望的键
                    expected_key = key // 2

                    # 如果没找到期望的键，或者期望的键数量不够，则肯定不行
                    if expected_key not in counter.keys() or counter[expected_key] < counter[key]:
                        return False

                    # 如果期望的键的数量正好够，则删掉这个期望的键
                    if counter[expected_key] == counter[key]:
                        del counter[expected_key]
                    else:  # 数量比key数量多，则干掉key数量的expected_key
                        counter[expected_key] -= counter[key]

                    # key被用完了，干掉
                    del counter[key]
                else:
                    break

        return True


if __name__ == '__main__':
    s = Solution()
    il = [
        [3, 1, 3, 6],
        [2, 1, 2, 6],
        [4, -2, 2, -4],
    ]
    for arr in il:
        pprint(s.canReorderDoubled(arr))
    pass
