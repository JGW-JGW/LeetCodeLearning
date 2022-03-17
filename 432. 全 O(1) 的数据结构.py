# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-16 10:04
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
from math import inf
import datetime as dt
import re
from abc import ABCMeta, abstractmethod
from collections import defaultdict

"""
请你设计一个用于存储字符串计数的数据结构，并能够返回计数最小和最大的字符串。

实现 AllOne 类：

AllOne() 初始化数据结构的对象。
inc(String key) 字符串 key 的计数增加 1 。如果数据结构中尚不存在 key ，那么插入计数为 1 的 key 。
dec(String key) 字符串 key 的计数减少 1 。如果 key 的计数在减少后为 0 ，那么需要将这个 key 从数据结构中删除。测试用例保证：在减少计数前，key 存在于数据结构中。
getMaxKey() 返回任意一个计数最大的字符串。如果没有元素存在，返回一个空字符串 "" 。
getMinKey() 返回任意一个计数最小的字符串。如果没有元素存在，返回一个空字符串 "" 。

提示：

1 <= key.length <= 10
key 由小写英文字母组成
测试用例保证：在每次调用 dec 时，数据结构中总存在 key
最多调用 inc、dec、getMaxKey 和 getMinKey 方法 5 * 10^4 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-oone-data-structure
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
问题主要出在 dec 上，如果 key 计数为1，此时 dec(key)

则必须删掉 key 这个键，那么 min_key 就会变成下一个
"""


class AllOne:
    def __init__(self):
        self.counter = defaultdict(int)
        self.list_of_count = [[] for _ in range(50000)]
        self.non_zero_index = set()

    def inc(self, key: str) -> None:
        if key not in self.counter:
            self.counter[key] = 1
            self.list_of_count[1].append(key)
            self.non_zero_index.add(1)
        else:
            self.list_of_count[self.counter[key]].remove(key)
            if len(self.list_of_count[self.counter[key]]) == 0:
                self.non_zero_index.remove(self.counter[key])
            self.counter[key] += 1
            self.list_of_count[self.counter[key]].append(key)
            self.non_zero_index.add(self.counter[key])

    def dec(self, key: str) -> None:
        if self.counter[key] > 1:
            self.list_of_count[self.counter[key]].remove(key)
            if len(self.list_of_count[self.counter[key]]) == 0:
                self.non_zero_index.remove(self.counter[key])
            self.counter[key] -= 1
            self.list_of_count[self.counter[key]].append(key)
            self.non_zero_index.add(self.counter[key])
        else:
            self.list_of_count[1].remove(key)
            if len(self.list_of_count[1]) == 0:
                self.non_zero_index.remove(1)
            del self.counter[key]

    def getMaxKey(self) -> str:
        return self.list_of_count[max(self.non_zero_index)][0] if len(self.non_zero_index) > 0 else ''

    def getMinKey(self) -> str:
        return self.list_of_count[min(self.non_zero_index)][0] if len(self.non_zero_index) > 0 else ''


class AllOne:
    def __init__(self):
        self.counter = defaultdict(int)
        self.set_of_count = [set() for _ in range(50000)]
        self.non_zero_index = set()

    def inc(self, key: str) -> None:
        if key not in self.counter:
            self.counter[key] = 1
            self.set_of_count[1].add(key)
            self.non_zero_index.add(1)
        else:
            self.set_of_count[self.counter[key]].remove(key)
            if len(self.set_of_count[self.counter[key]]) == 0:
                self.non_zero_index.remove(self.counter[key])
            self.counter[key] += 1
            self.set_of_count[self.counter[key]].add(key)
            self.non_zero_index.add(self.counter[key])

    def dec(self, key: str) -> None:
        if self.counter[key] > 1:
            self.set_of_count[self.counter[key]].remove(key)
            if len(self.set_of_count[self.counter[key]]) == 0:
                self.non_zero_index.remove(self.counter[key])
            self.counter[key] -= 1
            self.set_of_count[self.counter[key]].add(key)
            self.non_zero_index.add(self.counter[key])
        else:
            self.set_of_count[1].remove(key)
            if len(self.set_of_count[1]) == 0:
                self.non_zero_index.remove(1)
            del self.counter[key]

    def getMaxKey(self) -> str:
        if len(self.non_zero_index) > 0:
            for item in self.set_of_count[max(self.non_zero_index)]:
                return item
        return ''

    def getMinKey(self) -> str:
        if len(self.non_zero_index) > 0:
            for item in self.set_of_count[min(self.non_zero_index)]:
                return item
        return ''


if __name__ == '__main__':
    il = [
        (
            ["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"],
            [[], ["hello"], ["hello"], [], [], ["leet"], [], []]
        ),
        (
            ["AllOne", "getMaxKey", "getMinKey"],
            [[], [], []]
        )
    ]


    def call(instance: AllOne, funcname: str, param: List[str]):
        if funcname == 'AllOne':
            return None
        elif funcname == 'inc':
            instance.inc(param[0])
            return None
        elif funcname == 'getMaxKey':
            return instance.getMaxKey()
        elif funcname == 'getMinKey':
            return instance.getMinKey()
        elif funcname == 'dec':
            instance.dec(param[0])
            return None
        else:
            raise ValueError('错误的函数名：funcname = \"{}\"'.format(funcname))


    for t in il:
        all_one = AllOne()
        result = []
        for index in range(len(t[0])):
            result.append(call(all_one, t[0][index], t[1][index]))

        pprint(result)

    pass
