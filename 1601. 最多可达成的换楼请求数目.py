# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-02-28 11:07
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
我们有 n 栋楼，编号从 0 到 n - 1 。每栋楼有若干员工。由于现在是换楼的季节，部分员工想要换一栋楼居住。

给你一个数组 requests ，其中 requests[i] = [fromi, toi] ，表示一个员工请求从编号为 fromi 的楼搬到编号为 toi 的楼。

一开始 所有楼都是满的，所以从请求列表中选出的若干个请求是可行的需要满足 每栋楼员工净变化为 0 。意思是每栋楼 离开 的员工数目 等于 该楼 搬入 的员工数数目。比方说 n = 3 且两个员工要离开楼 0 ，一个员工要离开楼 1 ，一个员工要离开楼 2 ，如果该请求列表可行，应该要有两个员工搬入楼 0 ，一个员工搬入楼 1 ，一个员工搬入楼 2 。

请你从原请求列表中选出若干个请求，使得它们是一个可行的请求列表，并返回所有可行列表中最大请求数目。

1 <= n <= 20
1 <= requests.length <= 16
requests[i].length == 2
0 <= from_i, to_i <= n - 1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-number-of-achievable-transfer-requests
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def maximumRequests(n: int, requests: List[List[int]]) -> int:
        n_person = len(requests)
        max_num = 0
        for i in range(1 << n_person):
            io_dict = {}
            subset_length = 0
            for j in range(n_person):
                if i & (1 << j):
                    subset_length += 1
                    if requests[j][0] not in io_dict:
                        io_dict[requests[j][0]] = 1
                    else:
                        io_dict[requests[j][0]] += 1
                    if requests[j][1] not in io_dict:
                        io_dict[requests[j][1]] = -1
                    else:
                        io_dict[requests[j][1]] -= 1
            if all(value == 0 for value in io_dict.values()):
                max_num = max(max_num, subset_length)
        return max_num


if __name__ == '__main__':
    n = 5
    requests_list = [
        [[0, 1], [1, 0], [0, 1], [1, 2], [2, 0], [3, 4]],
        [[0, 0], [1, 2], [2, 1]],
        [[0, 3], [3, 1], [1, 2], [2, 0]],
    ]
    solution = Solution()
    for requests in requests_list:
        pprint(solution.maximumRequests(n, requests))

    pass
