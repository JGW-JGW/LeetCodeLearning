# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-29 20:38
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
一位老师正在出一场由 n 道判断题构成的考试，每道题的答案为 true （用 'T' 表示）或者 false （用 'F' 表示）。老师想增加学生对自己做出答案的不确定性，方法是 最大化 有 连续相同 结果的题数。（也就是连续出现 true 或者连续出现 false）。

给你一个字符串 answerKey ，其中 answerKey[i] 是第 i 个问题的正确结果。除此以外，还给你一个整数 k ，表示你能进行以下操作的最多次数：

每次操作中，将问题的正确答案改为 'T' 或者 'F' （也就是将 answerKey[i] 改为 'T' 或者 'F' ）。
请你返回在不超过 k 次操作的情况下，最大 连续 'T' 或者 'F' 的数目。

提示：

n == answerKey.length
1 <= n <= 5 * 10^4
answerKey[i] 要么是 'T' ，要么是 'F'   
1 <= k <= n

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximize-the-confusion-of-an-exam
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
滑动窗口

求修改次数不超过 k 的前提下，连续的 True 或 False 的最大长度
等价于
求一个包含不超过 k 个 False 或者 不超过 k 个 True 的最大窗口的长度

former 窗口左端点
latter 窗口右端点
"""


class Solution:
    @staticmethod
    def maxConsecutiveAnswers(answer_key: str, k: int) -> int:
        n = len(answer_key)

        def get_max_count_of_char(char: str) -> int:
            res = 0
            former = 0
            latter = 0
            count_of_char = 0
            while latter < n:
                if answer_key[latter] == char:
                    count_of_char += 1
                while count_of_char > k:
                    if answer_key[former] == char:
                        count_of_char -= 1
                    former += 1

                latter += 1

                res = max(res, latter - former)

            return res

        return max(get_max_count_of_char('F'), get_max_count_of_char('T'))


if __name__ == '__main__':
    s = Solution()
    il = [
        ('TTFF', 2),
        ('TFFT', 1),
        ('TTFTTFTT', 1),
    ]
    for t in il:
        pprint(s.maxConsecutiveAnswers(t[0], t[1]))
    pass
