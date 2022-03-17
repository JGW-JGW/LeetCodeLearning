# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-02-22 20:26
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

商 = 0
第1个值一定是 (a1 + b1 + 商) % 10
商可能为0或1
第2个值一定是 (a2 + b2 + 商) % 10

"""


class ListNode:
    # noinspection PyShadowingBuiltins
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# noinspection PyShadowingBuiltins
def list2num(num_list: List[int]) -> int:
    sum = 0
    for index in range(len(num_list)):
        sum += num_list[index] * 10 ** index
    return sum


def num2list(n: int) -> List[int]:
    result_list = []
    n_str = str(n)
    index = -1
    while -index <= len(n_str):
        result_list.append(int(n_str[index]))
        index -= 1
    return result_list


def num2node(n: int) -> ListNode:
    temp_list = []
    n_str = str(n)
    for index in range(-1, -len(n_str) - 1, -1):
        temp_list.append(int(n_str[index]))

    node = ListNode(temp_list[-1])
    for index in range(-2, -len(temp_list) - 1, -1):
        node = ListNode(temp_list[index], node)
    return node


class Solution:
    @staticmethod
    def node2list(ln: ListNode) -> List[int]:
        result_list = []

        while ln is not None:
            result_list.append(ln.val)
            ln = ln.next

        return result_list

    @staticmethod
    def list2node(num_list: List[int]) -> ListNode:
        node = ListNode(num_list[-1])
        for index in range(-2, -len(num_list) - 1, -1):
            node = ListNode(num_list[index], node)
        return node

    @staticmethod
    def add_two_lists(l1: List[int], l2: List[int]) -> List[int]:
        result_list = []
        n1 = len(l1)
        n2 = len(l2)
        quotient = 0
        if n1 > n2:
            for i in range(n2):
                remainder = (l1[i] + l2[i] + quotient) % 10
                result_list.append(remainder)
                quotient = int((l1[i] + l2[i] + quotient) / 10)
            for i in range(n2, n1):
                remainder = (l1[i] + quotient) % 10
                result_list.append(remainder)
                quotient = int((l1[i] + quotient) / 10)

        elif n1 < n2:
            for i in range(n1):
                remainder = (l1[i] + l2[i] + quotient) % 10
                result_list.append(remainder)
                quotient = int((l1[i] + l2[i] + quotient) / 10)
            for i in range(n1, n2):
                remainder = (l2[i] + quotient) % 10
                result_list.append(remainder)
                quotient = int((l2[i] + quotient) / 10)

        else:  # n1 == n2
            for i in range(n1):
                remainder = (l1[i] + l2[i] + quotient) % 10
                result_list.append(remainder)
                quotient = int((l1[i] + l2[i] + quotient) / 10)

        if quotient == 1:
            result_list.append(1)

        print(
            '===============================\n{}\n+ {}\n-------------------------------\n{}\n==============================='.format(
                list2num(l1),
                list2num(l2),
                list2num(result_list)
            ))

        return result_list

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.list2node(self.add_two_lists(self.node2list(l1), self.node2list(l2)))


class Solution1:
    @staticmethod
    def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
        curr = ListNode()
        head = curr
        carry = 0

        while carry != 0 or l1 is not None or l2 is not None:
            val = carry

            if l1 is not None:
                val += l1.val
                l1 = l1.next

            if l2 is not None:
                val += l2.val
                l2 = l2.next

            carry, val = divmod(val, 10)

            curr.next = ListNode(val)

            curr = curr.next

        return head.next


if __name__ == '__main__':
    s = Solution()

    input_list_1 = [
        123,
        0,
        987799,
        1
    ]

    input_list_2 = [
        321,
        0,
        8917239172983,
        9999999999999999999999999999999999999
    ]

    for i in range(len(input_list_1)):
        node1 = num2node(input_list_1[i])
        node2 = num2node(input_list_2[i])
        node_added = s.addTwoNumbers(node1, node2)
        l = s.node2list(node_added)
        n = list2num(l)
        print(n)
        # l1 = s.node2list(node1)
        # l2 = s.node2list(node2)
        # n1 = list2num(l1)
        # n2 = list2num(l2)
        # print('n1 = {}, n2 = {}'.format(n1, n2))

        # l1 = num2list(input_list[i])
        # l2 = num2list(input_list_1[i])
        # s.add_two_lists(l1, l2)

    pass
