# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-11 10:18
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
给你一棵根节点为 0 的 二叉树 ，它总共有 n 个节点，节点编号为 0 到 n - 1 。同时给你一个下标从 0 开始的整数数组 parents 表示这棵树，其中 parents[i] 是节点 i 的父节点。由于节点 0 是根，所以 parents[0] == -1 。

一个子树的 大小 为这个子树内节点的数目。每个节点都有一个与之关联的 分数 。求出某个节点分数的方法是，将这个节点和与它相连的边全部 删除 ，剩余部分是若干个 非空 子树，这个节点的 分数 为所有这些子树 大小的乘积 。

请你返回有 最高得分 节点的 数目 。

提示：

n == parents.length
2 <= n <= 105
parents[0] == -1
对于 i != 0 ，有 0 <= parents[i] <= n - 1
parents 表示一棵二叉树。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-nodes-with-the-highest-score
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
记编号为i的节点的左子树节点总数为：left[i]
记编号为i的节点的右子树节点总数为：right[i]
则以编号为i的节点为根的子树的节点总数为：1 + left[i] + right[i]
则删掉以编号为i的节点为根的子树之后，其余部分的节点总数：n - (1 + left[i] + right[i])
"""


class TreeNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def add_child(self, child):
        if self.left is None:
            self.left = child
        else:
            self.right = child


class Solution:
    max_score = 0
    n = 0
    n_of_max_score = 0

    # 判断节点数是否为0。如果为0，在计算分数时需要将0替换为1
    @staticmethod
    def trans(num: int) -> int:
        return num if num > 0 else 1

    # 深度优先搜索，求以当前节点为根的子树的总节点数
    def dfs(self, node: TreeNode) -> int:
        # 如果该节点不存在，则返回0
        if node is None:
            return 0

        left_total = self.dfs(node.left)
        right_total = self.dfs(node.right)
        remain = self.n - left_total - right_total - 1

        # 当前节点得分
        score = self.trans(left_total) * self.trans(right_total) * self.trans(remain)

        if score == self.max_score:
            self.n_of_max_score += 1
        elif score > self.max_score:
            self.n_of_max_score = 1
            self.max_score = score

        return left_total + right_total + 1

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.n = len(parents)

        # 索引相当于每个节点的id
        nodes = [TreeNode() for _ in range(self.n)]

        # 构造树
        for index in range(1, self.n):
            nodes[parents[index]].add_child(nodes[index])

        # 对树从根节点进行遍历，过程中会求出结果
        self.dfs(nodes[0])

        return self.n_of_max_score


class Solution1(object):
    max_score = 0
    n_of_max_score = 0
    n_of_nodes = 0

    @staticmethod
    def trans(num: int) -> int:
        return num if num > 0 else 1

    def dfs(self, node: int, lefts: List[int], rights: List[int]) -> int:
        if node == -1:
            return 0

        left_total = self.dfs(lefts[node], lefts, rights)
        right_total = self.dfs(rights[node], lefts, rights)
        remain = self.n_of_nodes - left_total - right_total - 1

        score = self.trans(left_total) * self.trans(right_total) * self.trans(remain)

        if score == self.max_score:
            self.n_of_max_score += 1
        elif score > self.max_score:
            self.n_of_max_score = 1
            self.max_score = score

        return left_total + right_total + 1

    def countHighestScoreNodes(self, parents: List[int]) -> int:
        self.n_of_nodes = len(parents)
        lefts = [-1] * self.n_of_nodes
        rights = [-1] * self.n_of_nodes

        # 构造树
        for index in range(1, self.n_of_nodes):
            if lefts[parents[index]] == -1:
                lefts[parents[index]] = index
            else:
                rights[parents[index]] = index

        # DFS
        self.dfs(0, lefts, rights)

        return self.n_of_max_score


if __name__ == '__main__':
    il = [
        [-1, 2, 0, 2, 0],
        [-1, 2, 0],
    ]

    for parents in il:
        s = Solution1()
        pprint(s.countHighestScoreNodes(parents))
