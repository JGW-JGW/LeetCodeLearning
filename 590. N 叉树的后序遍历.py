# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-12 12:10
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
from collections import defaultdict

"""
给定一个 n 叉树的根节点 root ，返回 其节点值的 后序遍历 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    @staticmethod
    def postorder(root: 'Node') -> List[int]:
        result = []

        def traversal(node: Node):
            if node is None:
                return

            for child in node.children:
                traversal(child)

            result.append(node.val)

        traversal(root)

        return result


"""
非递归思路：
二叉树：根入栈 → 右子节点入栈 → 左子节点入栈 → 顺序出栈
"""


class Solution:
    @staticmethod
    def postorder(root: 'Node') -> List[int]:
        if root is None:
            return []

        # 用来记录各节点的所有子节点是否都遍历完毕
        traversal_record = defaultdict(bool)

        result = []

        # 模拟栈
        stack = [root]

        while stack:
            cur_node = stack[-1]
            if traversal_record[cur_node]:
                result.append(cur_node.val)
                del stack[-1]
                continue

            for item in cur_node.children[::-1]:
                stack.append(item)

            traversal_record[cur_node] = True

        return result


if __name__ == '__main__':
    pass
