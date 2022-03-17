# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.10 16:56
# Author  : Seto.Kaiba
from pprint import pprint
import random
import math

"""
给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

 

进阶：

尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。
你可以使用空间复杂度为 O(1) 的 原地 算法解决这个问题吗？
 

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右旋转 1 步: [7,1,2,3,4,5,6]
向右旋转 2 步: [6,7,1,2,3,4,5]
向右旋转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右旋转 1 步: [99,-1,-100,3]
向右旋转 2 步: [3,99,-1,-100]
 

提示：

1 <= nums.length <= 2 * 104
-231 <= nums[i] <= 231 - 1
0 <= k <= 105

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2skh7/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


class Solution:
    def rotate(self, nums: list, k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # slice是浅拷贝，无法修改函数外nums的值，以下方式可以原地修改
        # if k != 0:
        #     nums[:] = nums[-k:] + nums[:len(nums) - k]

        # 整体颠倒，局部颠倒
        # nums[:] = nums[::-1]
        # nums[:k] = nums[:k][::-1]
        # nums[k:] = nums[k:][::-1]

        # 原地工作
        if k != 0:
            counter = 0
            start = 0
            while counter < n:
                cur = start
                buffer = nums[start]
                while True:
                    counter += 1
                    goal_pos = (cur + k) % n
                    nums[goal_pos], buffer = buffer, nums[goal_pos]
                    cur = goal_pos
                    if cur == start:
                        start += 1
                        break


if __name__ == '__main__':
    nums = [random.randint(1, 100) for i in range(random.randint(4, 8))]
    k = random.randint(2, 4)
    print(k)
    print(k % len(nums))
    print(nums)
    solution = Solution()
    solution.rotate(nums, k)
    print(nums)

    pass
