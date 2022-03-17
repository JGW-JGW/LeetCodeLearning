# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-06 09:34
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
你和一群强盗准备打劫银行。给你一个下标从 0 开始的整数数组 security ，其中 security[i] 是第 i 天执勤警卫的数量。日子从 0 开始编号。同时给你一个整数 time 。

如果第 i 天满足以下所有条件，我们称它为一个适合打劫银行的日子：

第 i 天前和后都分别至少有 time 天。
第 i 天前连续 time 天警卫数目都是非递增的。
第 i 天后连续 time 天警卫数目都是非递减的。
更正式的，第 i 天是一个合适打劫银行的日子当且仅当：security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].

请你返回一个数组，包含 所有 适合打劫银行的日子（下标从 0 开始）。返回的日子可以 任意 顺序排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-good-days-to-rob-the-bank
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
如果2*time >= len(security)，那么返回空列表
"""


class Solution:  # 暴力解法超时了
    @staticmethod
    def is_a_nice_day(security: List[int], time: int, index: int) -> bool:
        for i in range(index - time, index):
            if security[i] < security[i + 1]:
                return False
        for i in range(index, index + time):
            if security[i] > security[i + 1]:
                return False

        return True

    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)

        if 2 * time >= n:
            return []

        rob_days = []

        for day in range(time, n - time):
            if self.is_a_nice_day(security, time, day):
                rob_days.append(day)

        return rob_days


"""
i从0开始，即第0天、第1天……
记第 i-1 天之前连续非递增的天数为left[i-1]
如果第 i 天的警卫数量 <= 第 i-1 天的警卫数量，则：
left[i] = left[i-1] + 1
否则：
left[i] = 0

记第 i+1 天之后连续非递减的天数为right[i+1]
如果第 i 天的警卫数量 <= 第 i+1 天的警卫数量，则：
right[i] = right[i+1] + 1
否则：
right[i] = 0

"""


class Solution1(object):
    @staticmethod
    def goodDaysToRobBank(security: List[int], time: int) -> List[int]:
        n = len(security)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        for i in range(1, n):
            if security[i] <= security[i - 1]:
                left[i] = left[i - 1] + 1
            if security[n - i] >= security[n - i - 1]:
                right[n - i - 1] = right[n - i] + 1

        return [day for day in range(n) if left[day] >= time and right[day] >= time]


if __name__ == '__main__':
    s = Solution1()
    s = Solution()
    input_list = [
        ([5, 3, 3, 3, 5, 6, 2], 2),
        ([1, 1, 1, 1, 1], 0),
        ([1, 2, 3, 4, 5, 6], 2),
        ([1], 5),
    ]

    for t in input_list:
        pprint(s.goodDaysToRobBank(t[0], t[1]))

    pass
