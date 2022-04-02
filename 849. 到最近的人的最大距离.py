# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-04-02 13:15
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个数组 seats 表示一排座位，其中 seats[i] = 1 代表有人坐在第 i 个座位上，seats[i] = 0 代表座位 i 上是空的（下标从 0 开始）。

至少有一个空座位，且至少有一人已经坐在座位上。

亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。

返回他到离他最近的人的最大距离。

提示：

2 <= seats.length <= 2 * 10^4
seats[i] 为 0 或 1
至少有一个 空座位
至少有一个 座位上有人

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximize-distance-to-closest-person
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def maxDistToClosest(seats: List[int]) -> int:
        n = len(seats)
        # 获取从左边开始到第一个人之间的连续的 0 的数量
        left_zero = 0
        while seats[left_zero] == 0:
            left_zero += 1

        index_of_left_1st_person = left_zero

        # 获取从右边开始到第一个人之间的连续的 0 的数量
        right_zero = -1
        while seats[right_zero] == 0:
            right_zero -= 1

        index_of_right_1st_person = n + right_zero
        right_zero = - right_zero - 1

        max_count_of_continuous_zero = 0
        cur_count = 0
        for i in range(index_of_left_1st_person + 1, index_of_right_1st_person + 1):
            if seats[i] == 0:
                cur_count += 1
            else:  # 遇到了 1
                max_count_of_continuous_zero = max(max_count_of_continuous_zero, cur_count)
                cur_count = 0

        distance = max_count_of_continuous_zero // 2 if max_count_of_continuous_zero & 1 == 0 else (max_count_of_continuous_zero // 2 + 1)

        return max(left_zero, right_zero, distance)


if __name__ == '__main__':
    s = Solution()

    il = [
        # [1, 0, 0, 0, 1, 0, 1],
        # [1, 0, 0, 0],
        # [0, 1],
        # [1, 0, 0, 1, 1],
        [1, 0, 1]
    ]

    for seats in il:
        pprint(s.maxDistToClosest(seats))

    pass
