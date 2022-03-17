# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-14 10:11
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
from math import inf
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
假设 Andy 和 Doris 想在晚餐时选择一家餐厅，并且他们都有一个表示最喜爱餐厅的列表，每个餐厅的名字用字符串表示。

你需要帮助他们用最少的索引和找出他们共同喜爱的餐厅。 如果答案不止一个，则输出所有答案并且不考虑顺序。 你可以假设答案总是存在。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-index-sum-of-two-lists
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# class Solution:
#     @staticmethod
#     def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
#         return list(set(list1).intersection(set(list2)))


"""
索引和最小

先求出两个list的长度

遍历长度较小的list

用dict记录共同喜爱的餐厅及索引和
"""


class Solution:
    @staticmethod
    def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
        common_set = set(list1).intersection(set(list2))

        restaurant_names = []
        min_sum_of_index = inf

        for common in common_set:
            index1 = list1.index(common)
            index2 = list2.index(common)
            sum_of_index = index1 + index2
            if sum_of_index < min_sum_of_index:
                restaurant_names = [common]
                min_sum_of_index = sum_of_index
            elif sum_of_index == min_sum_of_index:
                restaurant_names.append(common)

        return restaurant_names


"""
构造字典存放
"""


class Solution:
    @staticmethod
    def findRestaurant(list1: List[str], list2: List[str]) -> List[str]:
        if len(list1) <= len(list2):
            target = list1
            another = list2
        else:
            target = list2
            another = list1

        record = {name: index for index, name in enumerate(target)}

        common_restaurants = []

        min_sum_of_index = inf

        for index, name in enumerate(another):
            if name in record:
                index_sum = record[name] + index
                if index_sum < min_sum_of_index:
                    common_restaurants = [name]
                    min_sum_of_index = index_sum
                elif index_sum == min_sum_of_index:
                    common_restaurants.append(name)

        return common_restaurants


if __name__ == '__main__':
    il = [
        (
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
        ),
        (
            ["Shogun", "Tapioca Express", "Burger King", "KFC"],
            ["KFC", "Shogun", "Burger King"]
        ),
    ]

    for t in il:
        s = Solution()
        pprint(s.findRestaurant(t[0], t[1]))
    pass
