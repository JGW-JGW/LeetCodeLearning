# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-15 13:58
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
from math import inf
from functools import reduce
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
import threading

"""
给你一个整数数组 nums ，请你找出 nums 子集 按位或 可能得到的 最大值 ，并返回按位或能得到最大值的 不同非空子集的数目 。

如果数组 a 可以由数组 b 删除一些元素（或不删除）得到，则认为数组 a 是数组 b 的一个 子集 。如果选中的元素下标位置不一样，则认为两个子集 不同 。

对数组 a 执行 按位或 ，结果等于 a[0] OR a[1] OR ... OR a[a.length - 1]（下标从 0 开始）。

提示：

1 <= nums.length <= 16
1 <= nums[i] <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-number-of-maximum-bitwise-or-subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
考虑到最多只有16个数字，则可以使用模拟法，所有非空子集的数量为2^16 - 1 = 65535

把 1 ~ 65535 转化为一个长度为 16 的序列：
1 → [False, False, ..., False, True] 15个False + 1个True
65535 → [True, ..., True] 16个True
"""


class Solution:
    @staticmethod
    def countMaxOrSubsets(nums: List[int]) -> int:
        n = len(nums)

        def num2list(num: int) -> List[bool]:
            result = [num & 1 == 1]
            for i in range(1, n):
                result.append(num >> i & 1 == 1)

            return result

        max_or_value = -inf
        max_count = 0

        for num in range(1, 2 ** n):
            index_flag = num2list(num)
            cur_or_value = 0
            for index in range(n):
                if index_flag[index]:
                    cur_or_value |= nums[index]

            if cur_or_value > max_or_value:
                max_count = 1
                max_or_value = cur_or_value
            elif cur_or_value == max_or_value:
                max_count += 1

        return max_count


"""
所有元素按位或的结果一定是最大值，所以可以提前获得最大值
"""


class Solution:
    @staticmethod
    def countMaxOrSubsets(nums: List[int]) -> int:
        n = len(nums)
        max_or_value = 0
        for num in nums:
            max_or_value |= num

        ans = 0

        for mask in range(1 << n):
            cur_or_value = 0
            for index in range(n):
                if mask >> index & 1 == 1:
                    cur_or_value |= nums[index]
            if cur_or_value == max_or_value:
                ans += 1

        return ans


"""
回溯法
"""


class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, nums: List[int], n: int, index: int, cur_or_value: int, max_or_value: int):
        if index == n:
            if cur_or_value == max_or_value:
                self.ans += 1
            return

        # 选中 nums[i]
        self.dfs(nums, n, index + 1, cur_or_value | nums[index], max_or_value)

        # 不选 nums[i]
        self.dfs(nums, n, index + 1, cur_or_value, max_or_value)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or_value = 0
        for item in nums:
            max_or_value |= item

        self.dfs(nums, n, 0, 0, max_or_value)

        return self.ans


"""
如果搜索到某个下标i时，如果计算结果已经为最大值，则利用数学计算结果
"""


class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, nums: List[int], n: int, index: int, cur_or_value: int, max_or_value: int):
        if cur_or_value == max_or_value:
            self.ans += 1 << (n - index)
            return
        if index == n:
            return

        # 选中 nums[i]
        self.dfs(nums, n, index + 1, cur_or_value | nums[index], max_or_value)

        # 不选 nums[i]
        self.dfs(nums, n, index + 1, cur_or_value, max_or_value)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or_value = 0
        for item in nums:
            max_or_value |= item

        self.dfs(nums, n, 0, 0, max_or_value)

        return self.ans


"""
跳过前面多个不选的情况
"""


class Solution:
    def __init__(self):
        self.ans = 0

    def dfs(self, nums: List[int], n: int, index: int, cur_or_value: int, max_or_value: int):
        if cur_or_value == max_or_value:
            self.ans += 1 << (n - index)
            return

        for j in range(index, n):
            self.dfs(nums, n, j + 1, cur_or_value | nums[j], max_or_value)

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or_value = 0
        for item in nums:
            max_or_value |= item

        self.dfs(nums, n, 0, 0, max_or_value)

        return self.ans


"""
多线程试一下
"""


class Solution:
    def __init__(self):
        self.ans = 0

    def check_or_value(self, nums: List[int], n: int, combo_value: int, max_or_value: int):
        cur_or_value = 0
        for index in range(n):
            if combo_value >> index & 1 == 1:
                cur_or_value |= nums[index]

        if cur_or_value == max_or_value:
            self.ans += 1

    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)
        max_or_value = 0
        for item in nums:
            max_or_value |= item

        for i in range(1, 1 << n):
            th = threading.Thread(target=self.check_or_value, args=(nums, n, i, max_or_value))
            th.start()

        return self.ans


if __name__ == '__main__':
    il = [
        [3, 1],
        [2, 2, 2],
        [3, 2, 1, 5],
    ]

    for nums in il:
        s = Solution()
        pprint(s.countMaxOrSubsets(nums))
