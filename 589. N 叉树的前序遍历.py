# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-10 10:21
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
给定一个 n 叉树的根节点  root ，返回 其节点值的 前序遍历 。

n 叉树 在输入中按层序遍历进行序列化表示，每组子节点由空值 null 分隔（请参见示例）。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


"""
递归思路：
二叉树前序遍历：根 → 左 →右
N叉树前序遍历：根 → 从左至右依次遍历
"""


class Solution:
    @staticmethod
    def preorder(root: 'Node') -> List[int]:
        result_list = []

        def traversal(node: Node):
            if node is None:
                return
            result_list.append(node.val)
            for child in node.children:
                traversal(child)

        traversal(root)

        return result_list


"""
非递归思路：
二叉树：右子节点入栈 → 左子节点入栈 → 输出当前节点
"""


class Solution:
    @staticmethod
    def preorder(root: 'Node') -> List[int]:
        if root is None:
            return []
        result_list = []
        stack = [root]
        while stack:
            cur_node = stack.pop()
            result_list.append(cur_node.val)
            for child in cur_node.children[::-1]:
                stack.append(child)

        return result_list


if __name__ == '__main__':
    pass
