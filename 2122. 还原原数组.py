# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-14 10:48
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
from collections import Counter, defaultdict
from copy import deepcopy

"""
Alice 有一个下标从 0 开始的数组 arr ，由 n 个正整数组成。她会选择一个任意的 正整数 k 并按下述方式创建两个下标从 0 开始的新整数数组 lower 和 higher ：

对每个满足 0 <= i < n 的下标 i ，lower[i] = arr[i] - k
对每个满足 0 <= i < n 的下标 i ，higher[i] = arr[i] + k
不幸地是，Alice 丢失了全部三个数组。但是，她记住了在数组 lower 和 higher 中出现的整数，但不知道每个整数属于哪个数组。请你帮助 Alice 还原原数组。

给你一个由 2n 个整数组成的整数数组 nums ，其中 恰好 n 个整数出现在 lower ，剩下的出现在 higher ，还原并返回 原数组 arr 。如果出现答案不唯一的情况，返回 任一 有效数组。

注意：生成的测试用例保证存在 至少一个 有效数组 arr 。

提示：

2 * n == nums.length
1 <= n <= 1000
1 <= nums[i] <= 10^9
生成的测试用例保证存在 至少一个 有效数组 arr

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-the-original-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
不妨假设arr[0] <= ... <= arr[i] <= ... <= arr[n-1]
则可得：
lower[0] <= ... <= lower[i] <= ... <= lower[n-1]
higher[0] <= ... <= higher[i] <= ... <= higher[n-1]
lower[i] < higher[i]

nums由lower和higher乱序组成，则有：
min(nums) = lower[0]
max(nums) = higher[n-1]

假设能找到lower[0]对应的higher[0]，则将这两个数字去除，得到nums_1，则：
min(nums_1) = lower[1]
max(nums_1) = higher[1]

问题变成了在已知lower[0]的情况下如何确定higher[0]
"""


class Solution:
    def __init__(self):
        self.arr = []

    def check_key_as_higher0(self, counter: Dict[int, int], key: int, lower0: int, keys) -> bool:
        """
        检查将counter中的键 key 作为higher[0]的可行性
        如果可行，返回True；否则返回False
        :param keys: 排序后的counter的keys
        :param lower0: lower[0]
        :param counter: nums的计数器
        :param key: 整数，counter中的键，key > lower0
        :return: True-可行 False-不可行
        """
        diff = key - lower0

        if diff & 1 == 1:  # 差为奇数时，返回False
            self.arr = []
            return False

        # 到这里说明差为偶数，此时可求出k
        k = diff // 2

        # 对counter进行深拷贝，防止原来的counter被篡改
        counter_copy = deepcopy(counter)

        # 从counter当中对某键的计数减1，如果计数减到0则删除该键
        def del_key_from_counter(key: int):
            if key in counter_copy:
                if counter_copy[key] > 1:
                    counter_copy[key] -= 1
                else:  # counter_copy[key] == 1，减1后为0，删除key
                    del counter_copy[key]

        del_key_from_counter(lower0)
        del_key_from_counter(key)
        self.arr.append(lower0 + k)

        for item in keys:
            while item in counter_copy:
                higher = item + 2 * k
                if higher in counter_copy:  # 能找到合法的higher，则删除这一对
                    del_key_from_counter(item)
                    del_key_from_counter(higher)
                    self.arr.append(item + k)
                else:  # 找不到合法的higher，则直接返回False
                    self.arr = []
                    return False

        return True

    def recoverArray(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        keys = sorted(counter.keys())
        n_keys = len(keys)
        lower0 = keys[0]

        for index in range(1, n_keys):
            if self.check_key_as_higher0(counter=counter, key=keys[index], lower0=lower0, keys=keys):
                return self.arr


class Solution:
    @staticmethod
    def recoverArray(nums: List[int]) -> List[int]:
        nums.sort()
        for e in nums:
            diff = e - nums[0]
            if diff == 0 or diff & 1 == 1:
                continue
            delete_count = defaultdict(int)
            # 元素值 -> 要删除的这种值的数量
            ans = []

            for ee in nums:
                # 当遍历到ee时，如果delete_count[ee] >= 1，说明之前有个 ee - diff 对删除ee提出了要求，此时匹配成功，计数器减1
                # 匹配成功也意味着找到了一对合法的lower和higher，需要将对应的原始arr值记录到结果中
                if delete_count[ee] >= 1:
                    delete_count[ee] -= 1
                    ans.append(ee - diff // 2)

                # 当遍历到ee时，如果delete_count[ee] == 0，说明第一次遇到ee，则需要删除一个 ee + diff，计数器加1
                else:
                    delete_count[ee + diff] += 1

            # 验证是否全部配对成功
            if sum(delete_count.values()) == 0:
                return ans


class Solution:
    @staticmethod
    def recoverArray(nums: List[int]) -> List[int]:
        nums.sort()
        i, n = 1, len(nums)

        while True:
            if nums[i] == nums[i - 1]:
                i += 1
                continue

            diff = nums[i] - nums[0]

            if diff & 1 > 0:
                i += 1
                continue

            # 记录 nums 中属于 higher 的数的位置
            in_higher = [False] * n

            # 一开始就是验证 nums[i] 作为 higher[0] 的可行性，所以需要添加 i 到 in_higher 中
            in_higher[i] = True

            k = diff >> 1

            result = [nums[0] + k]

            lo, hi = 1, i + 1

            while hi < n:
                # 当 lo 在 n 范围内且lo位置已经被添加到 higher 中
                while lo < n and in_higher[lo]:
                    lo += 1

                # 当找到了一个 lo 之后，寻找匹配的 hi。只要差值比 diff 小，就继续看下一个
                while hi < n and nums[hi] - nums[lo] < diff:
                    hi += 1

                # 如果 hi 到达 n，说明没找到合适的 hi；或者没找到差值正好等于 diff 的 hi，则退出循环
                if hi == n or nums[hi] - nums[lo] > diff:
                    break

                # 恰好找到了合适的 hi
                in_higher[hi] = True

                result.append(nums[lo] + k)

                lo += 1
                hi += 1

            if len(result) == n >> 1:
                return result

            i += 1


if __name__ == '__main__':
    il = [
        # [2, 10, 6, 4, 8, 12],
        # [1, 1, 3, 3],
        # [5, 435],
        [1, 50, 99, 101, 150, 199],
    ]

    for nums in il:
        s = Solution()
        pprint(s.recoverArray(nums))

    pass
