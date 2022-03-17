# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.11 19:48
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2jrse/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def twoSum(nums: List[int], target: int) -> List[int]:
    # 这段代码针对[3,1,1] 6和[3,2,3] 6无法验证通过
    # n = len(nums)
    # for i in range(n):
    #     another = target - nums[i]
    #     try:
    #         index = nums.index(another)
    #         if index != i:
    #             return [i, index]
    #     except ValueError as e:
    #         return []

    # 暴力算法 通过 但时空效率low爆
    # n = len(nums)
    # for i in range(n - 1):
    #     another = target - nums[i]
    #     temp_list = nums[i+1:]
    #     if another in temp_list:
    #         return [i, i+1+temp_list.index(another)]

    # 仿照HashMap用字典
    hash_dict = dict()
    for index, value in enumerate(nums):
        another = target - value
        if hash_dict.get(another) is None:
            hash_dict[value] = index
        else:
            return [index, hash_dict[another]]


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    pprint(twoSum(nums, target))
    pass
