# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-21 14:27
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict, Optional
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个二叉搜索树 root 和一个目标结果 k，如果 BST 中存在两个元素且它们的和等于给定的目标结果，则返回 true。

提示:

二叉树的节点个数的范围是  [1, 10^4].
-10^4 <= Node.val <= 10^4
root 为二叉搜索树
-10^5 <= k <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def findTarget(root: Optional[TreeNode], k: int) -> bool:
        record_list = []

        def traversal(node: TreeNode) -> None:
            if node:
                traversal(node.left)
                record_list.append(node.val)
                traversal(node.right)

        traversal(root)

        left, right = 0, len(record_list) - 1

        while left < right:
            s = record_list[left] + record_list[right]

            if s == k:
                return True

            if s < k:
                left += 1

            else:
                right -= 1

        return False


if __name__ == '__main__':
    pass
