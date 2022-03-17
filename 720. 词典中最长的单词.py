# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-17 08:29
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
给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。

若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。

提示：

1 <= words.length <= 1000
1 <= words[i].length <= 30
所有输入的字符串 words[i] 都只包含小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-word-in-dictionary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def longestWord(words: List[str]) -> str:
        # 由于每个单词的长度为 1 至 30 个字符
        # 令  1 对应 长度为  1 的单词的集合
        # 令  i 对应 长度为  i 的单词的集合
        # 令 30 对应 长度为 30 的单词的集合
        set_based_on_length = [set() for _ in range(31)]

        for word in words:
            set_based_on_length[len(word)].add(word)

        for length in range(30, 0, -1):
            if set_based_on_length[length]:
                longest_words = []
                for item in set_based_on_length[length]:
                    flag = True
                    for each_length in range(1, length):
                        if item[:each_length] not in set_based_on_length[each_length]:
                            flag = False
                            break
                    if flag:
                        longest_words.append(item)
                if longest_words:
                    return min(longest_words)

        return ''


class Solution:
    @staticmethod
    def longestWord(words: List[str]) -> str:
        set_based_on_length = defaultdict(set)

        for word in words:
            set_based_on_length[len(word)].add(word)

        for length in sorted(set_based_on_length.keys(), reverse=True):
            longest_words = set()
            for word in set_based_on_length[length]:
                flag = True
                for each_length in range(1, length):
                    if each_length not in set_based_on_length or word[:each_length] not in set_based_on_length[
                        each_length]:
                        flag = False
                        break
                if flag:
                    longest_words.add(word)
            if longest_words:
                return min(longest_words)

        return ''


class Solution:
    @staticmethod
    def longestWord(words: List[str]) -> str:
        set_based_on_length = defaultdict(set)

        for word in words:
            set_based_on_length[len(word)].add(word)

        for length in sorted(set_based_on_length.keys(), reverse=True):
            min_word = ''.join(['z' for _ in range(length + 1)])
            for word in set_based_on_length[length]:
                flag = True
                for each_length in range(1, length):
                    if each_length not in set_based_on_length or word[:each_length] not in set_based_on_length[
                        each_length]:
                        flag = False
                        break
                if flag and word < min_word:
                    min_word = word
            if len(min_word) == length:
                return min_word

        return ''


class Solution:
    @staticmethod
    def longestWord(words: List[str]) -> str:
        words.sort()
        word_set, longest_word = {''}, ''
        for word in words:
            if word[:-1] in word_set:
                word_set.add(word)
                if len(word) > len(longest_word):
                    longest_word = word

        return longest_word


if __name__ == '__main__':
    il = [
        ["w", "wo", "wor", "worl", "world"],
        ["a", "banana", "app", "appl", "ap", "apply", "apple"],
        ["a", "banana", "app", "appl", "ap", "apply", "apple"],
        ["wo", "wor", "worl", "world"],
    ]

    s = Solution()

    for words in il:
        pprint(s.longestWord(words))

    pass
