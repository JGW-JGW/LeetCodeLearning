# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-21 13:56
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict, Optional, Union
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
你需要采用前序遍历的方式，将一个二叉树转换成一个由括号和整数组成的字符串。

空节点则用一对空括号 "()" 表示。而且你需要省略所有不影响字符串与原始二叉树之间的一对一映射关系的空括号对。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-string-from-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def tree2str(root: Optional[TreeNode]) -> str:
        res_list = []

        def traversal(node: TreeNode):
            if node is None:
                return

            res_list.append(str(node.val))

            if node.left is not None and node.right is not None:
                res_list.append('(')
                traversal(node.left)
                res_list.append(')(')
                traversal(node.right)
                res_list.append(')')

            elif node.left is None and node.right is not None:
                res_list.append('()(')
                traversal(node.right)
                res_list.append(')')

            elif node.left is not None and node.right is None:
                res_list.append('(')
                traversal(node.left)
                res_list.append(')')

        traversal(root)

        return ''.join(res_list)


if __name__ == '__main__':
    node1_4 = TreeNode(val=4)
    node1_2 = TreeNode(val=2, left=node1_4)
    node1_3 = TreeNode(val=3)
    root1 = TreeNode(val=1, left=node1_2, right=node1_3)

    node2_4 = TreeNode(val=4)
    node2_2 = TreeNode(val=2, right=node2_4)
    node2_3 = TreeNode(val=3)
    root2 = TreeNode(val=1, left=node2_2, right=node2_3)

    s = Solution()

    pprint(s.tree2str(root2))

    pass
