# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-30 20:34
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
你有 k 个服务器，编号为 0 到 k-1 ，它们可以同时处理多个请求组。每个服务器有无穷的计算能力但是 不能同时处理超过一个请求 。请求分配到服务器的规则如下：

第 i （序号从 0 开始）个请求到达。
如果所有服务器都已被占据，那么该请求被舍弃（完全不处理）。
如果第 (i % k) 个服务器空闲，那么对应服务器会处理该请求。
否则，将请求安排给下一个空闲的服务器（服务器构成一个环，必要的话可能从第 0 个服务器开始继续找下一个空闲的服务器）。比方说，如果第 i 个服务器在忙，那么会查看第 (i+1) 个服务器，第 (i+2) 个服务器等等。
给你一个 严格递增 的正整数数组 arrival ，表示第 i 个任务的到达时间，和另一个数组 load ，其中 load[i] 表示第 i 个请求的工作量（也就是服务器完成它所需要的时间）。你的任务是找到 最繁忙的服务器 。最繁忙定义为一个服务器处理的请求数是所有服务器里最多的。

请你返回包含所有 最繁忙服务器 序号的列表，你可以以任意顺序返回这个列表。

提示：

1 <= k <= 10^5
1 <= arrival.length, load.length <= 10^5
arrival.length == load.length
1 <= arrival[i], load[i] <= 10^9
arrival 保证 严格递增 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-servers-that-handled-most-number-of-requests
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Server:
    max_job_count = 0
    most_hardworking_servers = []

    def __init__(self):
        self.job_count = 0
        # self.last_receipt_time = 0
        self.next_available_time = 0

    def receive_a_job(self, arrival_time: int, job_time: int, server_no: int) -> bool:
        # 没空干活，返回失败提示
        if not self.is_available(arrival_time):
            return False

        # 有空干活，则开始干活
        self.job_count += 1
        # self.last_receipt_time = arrival_time
        self.next_available_time = arrival_time + job_time

        if self.job_count > Server.max_job_count:
            Server.max_job_count = self.job_count
            Server.most_hardworking_servers = [server_no]
        elif self.job_count == Server.max_job_count:
            Server.most_hardworking_servers.append(server_no)

        return True

    def is_available(self, current_time: int) -> bool:
        return current_time >= self.next_available_time


class Solution:
    class Server:
        max_job_count = 0
        most_hardworking_servers = []

        def __init__(self):
            self.job_count = 0
            # self.last_receipt_time = 0
            self.next_available_time = 0

        def receive_a_job(self, arrival_time: int, job_time: int, server_no: int) -> bool:
            # 没空干活，返回失败提示
            if not self.is_available(arrival_time):
                return False

            # 有空干活，则开始干活
            self.job_count += 1
            # self.last_receipt_time = arrival_time
            self.next_available_time = arrival_time + job_time

            if self.job_count > Server.max_job_count:
                Server.max_job_count = self.job_count
                Server.most_hardworking_servers = [server_no]
            elif self.job_count == Server.max_job_count:
                Server.most_hardworking_servers.append(server_no)

            return True

        def is_available(self, current_time: int) -> bool:
            return current_time >= self.next_available_time

    @staticmethod
    def busiestServers(k: int, arrival: List[int], load: List[int]) -> List[int]:
        servers = [Server() for _ in range(k)]
        server_no_list = list(range(k))
        for job_no in range(len(arrival)):
            init_server_no = job_no % k
            for server_no in server_no_list[init_server_no:] + server_no_list[0:init_server_no]:
                if servers[server_no].is_available(arrival[job_no]):
                    servers[server_no].receive_a_job(arrival[job_no], load[job_no], server_no)
                    break

        res = Server.most_hardworking_servers
        Server.max_job_count = 0
        Server.most_hardworking_servers = []

        return res


"""
上面的模拟法，直接超时，还是抄作业吧
"""


class Solution:
    @staticmethod
    def busiestServers(k: int, arrival: List[int], load: List[int]) -> List[int]:
        pass


if __name__ == '__main__':
    il = [
        # (3, [1, 2, 3, 4, 5], [5, 2, 3, 3, 3]),
        # (3, [1, 2, 3, 4], [1, 2, 1, 2]),
        (3, [1, 2, 3], [10, 12, 11]),
        (3, [1, 2, 3, 4], [1, 2, 1, 2]),
    ]
    s = Solution()
    for t in il:
        pprint(s.busiestServers(t[0], t[1], t[2]))
    pass
