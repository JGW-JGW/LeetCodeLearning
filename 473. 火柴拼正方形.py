# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-06 16:51
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
你将得到一个整数数组 matchsticks ，其中 matchsticks[i] 是第 i 个火柴棒的长度。你要用 所有的火柴棍 拼成一个正方形。你 不能折断 任何一根火柴棒，但你可以把它们连在一起，而且每根火柴棒必须 使用一次 。

如果你能使这个正方形，则返回 true ，否则返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/matchsticks-to-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

提示:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 10^8
"""

"""
如果火柴数量小于4根，则返回False

求和，同时排序，如果火柴总长度不能被4整除，则返回False

正方形边长为商

如果最大值 > 商，返回False

[]
"""


# class Solution:
#     @staticmethod
#     def makesquare(matchsticks: List[int]) -> bool:
#         n = len(matchsticks)
#         if n < 4:
#             return False
#
#         c, counter = sum(matchsticks), Counter(matchsticks)
#
#         a, mod = divmod(c, 4)
#
#         if mod != 0 or max(counter.keys()) > a:
#             return False
#
#         a_list = [a, a, a, a]
#
#         for i in [0, 1, 2, 3]:
#             for key in sorted(counter.keys(), reverse=True):
#                 while a_list[i] >= key and counter[key] > 0:
#                     a_list[i] -= key
#                     counter[key] -= 1
#                 if a_list[i] == 0:
#                     break
#
#         return all(item == 0 for item in a_list)


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        c = sum(matchsticks)
        if c & 3 != 0:  # 判断是否能被4整除
            return False

        side = [0, 0, 0, 0]

        return self.backtrack(sorted(matchsticks, reverse=True), len(matchsticks), 0, c >> 2, side)

    def backtrack(self, nums: List[int], n: int, index: int, a: int, side: List[int]) -> bool:
        """
        返回是否可以组成正方形
        :param n: nums的长度
        :param nums: 每根火柴的长度形成的列表
        :param index: 当前被访问的火柴索引
        :param a: 正方形边长
        :param side: 长度为4的列表
        :return: True-可以组成正方形 False-不能组成正方形
        """

        # 如果已经访问到最后一根火柴，并且4条边长度相等，说明形成了正方形，直接返回True，否则返回False
        if index == n:
            return True

        # 还没有访问到最后一根火柴
        for i in range(4):
            # 如果把当前火柴放到size[i]这条边上，其长度大于边长，则跳过
            if side[i] + nums[index] > a or (i > 0 and side[i] == side[i - 1]):
                continue

            # 如果当前火柴放到size[i]上，长度小于等于边长，则将该火柴放在这条边上
            side[i] += nums[index]

            # 再放下一根火柴，如果最终能变成正方形，直接返回True
            if self.backtrack(nums, n, index + 1, a, side):
                return True

            # 如果当前火柴放到这条边上，最终不能构成正方形，则移除这根火柴，再试下一根
            side[i] -= nums[index]

        # 不能构成正方形，返回False
        return False


if __name__ == '__main__':
    s = Solution()
    input_list = [
        # [1, 1, 2, 2, 2],
        # [3, 3, 3, 3, 4],
        [5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3],
    ]
    for item in input_list:
        pprint(s.makesquare(item))
    pass
