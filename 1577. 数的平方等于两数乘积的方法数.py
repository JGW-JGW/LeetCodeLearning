# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-02-27 14:42
# Author  : Seto.Kaiba
from collections import Counter
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你两个整数数组 nums1 和 nums2 ，请你返回根据以下规则形成的三元组的数目（类型 1 和类型 2 ）：

 
 85/类型 1：三元组 (i, j, k) ，如果 nums1[i]^2 == nums2[j] * nums2[k] 其中 0 <= i < nums1.length 且 0 <= j < k < nums2.length
类型 2：三元组 (i, j, k) ，如果 nums2[i]^2 == nums1[j] * nums1[k] 其中 0 <= i < nums2.length 且 0 <= j < k < nums1.length

1 <= nums1.length, nums2.length <= 1000
1 <= nums1[i], nums2[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-ways-where-square-of-number-is-equal-to-product-of-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def numTriplets(nums1: List[int], nums2: List[int]) -> int:
        def get_triplets(map1: Counter, map2: Counter) -> int:
            result = 0
            for num1, count1 in map1.items():
                square = num1 * num1
                for num2, count2 in map2.items():
                    if square % num2 == 0:
                        num3 = square // num2
                        if num2 == num3:
                            result += int(count1 * count2 * (count2 - 1) / 2)
                        elif num2 < num3 and num3 in map2:
                            count3 = map2[num3]
                            result += count1 * count2 * count3

            return result

        map1 = Counter(nums1)
        map2 = Counter(nums2)

        return get_triplets(map1, map2) + get_triplets(map2, map1)


if __name__ == '__main__':
    n = 3
    input_list = []
    for _ in range(n):
        max_len = 1000
        min_len = 1
        random_len = rd.randint(min_len, max_len)

        max_value = 10 ** 5
        min_value = 1
        nums1 = [rd.randint(min_value, max_value) for _ in range(random_len)]
        nums2 = [rd.randint(min_value, max_value) for _ in range(random_len)]
        input_list.append((nums1, nums2))

    input_list.extend([
        (
            [7, 4],
            [5, 2, 8, 9]
        ),
    ])

    solution = Solution()

    for t in input_list:
        pprint(solution.numTriplets(t[0], t[1]))

    pass
