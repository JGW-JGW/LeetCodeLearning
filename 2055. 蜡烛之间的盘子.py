# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-08 17:52
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个长桌子，桌子上盘子和蜡烛排成一列。给你一个下标从 0 开始的字符串 s ，它只包含字符 '*' 和 '|' ，其中 '*' 表示一个 盘子 ，'|' 表示一支 蜡烛 。

同时给你一个下标从 0 开始的二维整数数组 queries ，其中 queries[i] = [lefti, righti] 表示 子字符串 s[lefti...righti] （包含左右端点的字符）。对于每个查询，你需要找到 子字符串中 在 两支蜡烛之间 的盘子的 数目 。如果一个盘子在 子字符串中 左边和右边 都 至少有一支蜡烛，那么这个盘子满足在 两支蜡烛之间 。

比方说，s = "||**||**|*" ，查询 [3, 8] ，表示的是子字符串 "*||**|" 。子字符串中在两支蜡烛之间的盘子数目为 2 ，子字符串中右边两个盘子在它们左边和右边 都 至少有一支蜡烛。
请你返回一个整数数组 answer ，其中 answer[i] 是第 i 个查询的答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/plates-between-candles
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:  # 碰到了一个很长的串和很多的查询，任务超时
    @staticmethod
    def platesBetweenCandles(s: str, queries: List[List[int]]) -> List[int]:
        result_list = []
        for interval in queries:
            plate_counter = 0
            plate_num_at_the_left_of_candle_list = []
            for char in s[interval[0]:interval[1] + 1]:
                if char == '*':
                    plate_counter += 1
                if char == '|':
                    plate_num_at_the_left_of_candle_list.append(plate_counter)

            result_list.append(
                plate_num_at_the_left_of_candle_list[-1] - plate_num_at_the_left_of_candle_list[0] if len(
                    plate_num_at_the_left_of_candle_list) > 0 else 0)

        return result_list


class Solution(object):
    # left_plate_num_list: 表示位置为i处，左侧（不包含当前位置）盘子的累计个数
    # nearest_left_candle_index_list: 表示位置为i处，左边最近（包含i）的蜡烛的位置
    # nearest_right_candle_index_list: 表示位置为i处，右边最近（包含i）的蜡烛的位置
    # 最终答案：查询区间右边界的左边最近的蜡烛的位置的左侧（不包含当前位置）子累计个数 减去
    #         查询区间左边界的右边最近的蜡烛的位置的左侧（不包含当前位置）盘子累计个数
    @staticmethod
    def platesBetweenCandles(s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        left_plate_num_list = [0 for _ in range(n)]
        nearest_left_candle_index_list = [0 for _ in range(n)]
        nearest_right_candle_index_list = [n - 1 for _ in range(n)]

        for index in range(0, n):
            if index > 0:
                if s[index - 1] == '*':
                    left_plate_num_list[index] = left_plate_num_list[index - 1] + 1
                else:
                    left_plate_num_list[index] = left_plate_num_list[index - 1]

            if s[index] == '|':
                nearest_left_candle_index_list[index] = index
            elif index > 0:
                nearest_left_candle_index_list[index] = nearest_left_candle_index_list[index - 1]

            if s[n - 1 - index] == '|':
                nearest_right_candle_index_list[n - 1 - index] = n - 1 - index
            elif index > 0:
                nearest_right_candle_index_list[n - 1 - index] = nearest_right_candle_index_list[n - index]

        result_list = []
        for interval in queries:
            result_list.append(
                left_plate_num_list[nearest_left_candle_index_list[interval[1]]] -
                left_plate_num_list[nearest_right_candle_index_list[interval[0]]]
                if nearest_left_candle_index_list[interval[1]] > interval[0] else 0
            )

        return result_list


if __name__ == '__main__':
    s = Solution()

    il = [
        (
            "||**||**|*",
            [[3, 8]]
        ),
        (
            '**|**|***|',
            [[2, 5], [5, 9]]
        ),
        (
            "***|**|*****|**||**|*",
            [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
        ),
        (
            '***',
            [[2, 2]]
        ),
    ]

    for tp in il:
        pprint(s.platesBetweenCandles(tp[0], tp[1]))

    pass
