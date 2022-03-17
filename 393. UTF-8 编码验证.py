# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-13 10:27
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个表示数据的整数数组 data ，返回它是否为有效的 UTF-8 编码。

UTF-8 中的一个字符可能的长度为 1 到 4 字节，遵循以下的规则：

对于 1 字节 的字符，字节的第一位设为 0 ，后面 7 位为这个符号的 unicode 码。
对于 n 字节 的字符 (n > 1)，第一个字节的前 n 位都设为1，第 n+1 位设为 0 ，后面字节的前两位一律设为 10 。剩下的没有提及的二进制位，全部为这个符号的 unicode 码。
这是 UTF-8 编码的工作方式：

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
注意：输入是整数数组。只有每个整数的 最低 8 个有效位 用来存储数据。这意味着每个整数只表示 1 字节的数据。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/utf-8-validation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def validUtf8(data: List[int]) -> bool:
        n_of_bytes = len(data)
        index = 0
        remaining_bytes = n_of_bytes
        while index < n_of_bytes:
            if data[index] >> 7 == 0:
                index += 1
                remaining_bytes -= 1
                continue

            if remaining_bytes > 1 and data[index] >> 5 == 0b110 and data[index + 1] >> 6 == 0b10:
                index += 2
                remaining_bytes -= 2
                continue

            if remaining_bytes > 2 and data[index] >> 4 == 0b1110 and data[index + 1] >> 6 == 0b10 and data[
                index + 2] >> 6 == 0b10:
                index += 3
                remaining_bytes -= 3
                continue

            if remaining_bytes > 3 and data[index] >> 3 == 0b11110 and data[index + 1] >> 6 == 0b10 and data[
                index + 2] >> 6 == 0b10 and data[index + 3] >> 6 == 0b10:
                index += 4
                remaining_bytes -= 4
                continue

            return False

        return True


class Solution:
    @staticmethod
    def validUtf8(data: List[int]) -> bool:
        n_of_bytes = len(data)

        index = 0
        while index < n_of_bytes:
            cur_byte = data[index]
            # 求当前字节的开头前5位有多少个连续的1
            pos = 7
            while pos > 2 and cur_byte >> pos & 1 == 1:
                pos -= 1
            count = 7 - pos

            # 如果连续的1有1个或5个，则返回False
            if count == 1 or count == 5:
                return False

            # 如果当前位置的后面的字节数不够用，则返回False
            if index + count - 1 >= n_of_bytes:
                return False

            for i in range(index + 1, index + count):
                if data[i] >> 6 == 0b10:
                    continue
                return False

            if count == 0:
                index += 1
            else:
                index += count

        return True


if __name__ == '__main__':
    il = [
        # [197, 130, 1],
        # [235, 140, 4],
        [237],
    ]

    for item in il:
        s = Solution()
        pprint(s.validUtf8(item))
    pass
