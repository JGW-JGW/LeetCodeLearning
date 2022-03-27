# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-26 10:18
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
你现在是一场采用特殊赛制棒球比赛的记录员。这场比赛由若干回合组成，过去几回合的得分可能会影响以后几回合的得分。

比赛开始时，记录是空白的。你会得到一个记录操作的字符串列表 ops，其中 ops[i] 是你需要记录的第 i 项操作，ops 遵循下述规则：

整数 x - 表示本回合新获得分数 x
"+" - 表示本回合新获得的得分是前两次得分的总和。题目数据保证记录此操作时前面总是存在两个有效的分数。
"D" - 表示本回合新获得的得分是前一次得分的两倍。题目数据保证记录此操作时前面总是存在一个有效的分数。
"C" - 表示前一次得分无效，将其从记录中移除。题目数据保证记录此操作时前面总是存在一个有效的分数。
请你返回记录中所有得分的总和。

提示：

1 <= ops.length <= 1000
ops[i] 为 "C"、"D"、"+"，或者一个表示整数的字符串。整数范围是 [-3 * 10^4, 3 * 10^4]
对于 "+" 操作，题目数据保证记录此操作时前面总是存在两个有效的分数
对于 "C" 和 "D" 操作，题目数据保证记录此操作时前面总是存在一个有效的分数

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/baseball-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/baseball-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
先暴力解决一下
"""


class Solution:
    @staticmethod
    def calPoints(ops: List[str]) -> int:
        valid_score = []
        for item in ops:
            if item[0] == '-' or item[0].isdigit():
                valid_score.append(int(item))
            elif item == 'C':
                del valid_score[-1]
            elif item == 'D':
                valid_score.append(valid_score[-1] * 2)
            elif item == '+':
                valid_score.append(valid_score[-1] + valid_score[-2])

        return sum(valid_score)


# noinspection PyPep8Naming
class Solution1:
    @staticmethod
    def calPoints(ops: List[str]) -> int:
        valid_score = []
        S = 0
        for item in ops:
            if item[0] == '-' or item[0].isdigit():
                score = int(item)
            elif item == 'C':
                S -= valid_score[-1]
                del valid_score[-1]
                continue
            elif item == 'D':
                score = valid_score[-1] * 2
            elif item == '+':
                score = valid_score[-1] + valid_score[-2]

            S += score

            valid_score.append(score)

        return sum(valid_score)


if __name__ == '__main__':
    s = Solution1()

    il = [
        ["5", "2", "C", "D", "+"],
        ["5", "-2", "4", "C", "D", "9", "+", "+"],
        ["1"],
    ]

    for ops in il:
        pprint(s.calPoints(ops))
    pass
