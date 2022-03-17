# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.21 22:49
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
请你来实现一个 myAtoi(string s) 函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数 myAtoi(string s) 的算法如下：

读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−231,  231 − 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −231 的整数应该被固定为 −231 ，大于 231 − 1 的整数应该被固定为 231 − 1 。
返回整数作为最终结果。
注意：

本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
 

示例 1：

输入：s = "42"
输出：42
解释：加粗的字符串为已经读入的字符，插入符号是当前读取的字符。
第 1 步："42"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："42"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："42"（读入 "42"）
           ^
解析得到整数 42 。
由于 "42" 在范围 [-231, 231 - 1] 内，最终结果为 42 。
示例 2：

输入：s = "   -42"
输出：-42
解释：
第 1 步："   -42"（读入前导空格，但忽视掉）
            ^
第 2 步："   -42"（读入 '-' 字符，所以结果应该是负数）
             ^
第 3 步："   -42"（读入 "42"）
               ^
解析得到整数 -42 。
由于 "-42" 在范围 [-231, 231 - 1] 内，最终结果为 -42 。
示例 3：

输入：s = "4193 with words"
输出：4193
解释：
第 1 步："4193 with words"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："4193 with words"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："4193 with words"（读入 "4193"；由于下一个字符不是一个数字，所以读入停止）
             ^
解析得到整数 4193 。
由于 "4193" 在范围 [-231, 231 - 1] 内，最终结果为 4193 。
示例 4：

输入：s = "words and 987"
输出：0
解释：
第 1 步："words and 987"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："words and 987"（当前没有读入字符，因为这里不存在 '-' 或者 '+'）
         ^
第 3 步："words and 987"（由于当前字符 'w' 不是一个数字，所以读入停止）
         ^
解析得到整数 0 ，因为没有读入任何数字。
由于 0 在范围 [-231, 231 - 1] 内，最终结果为 0 。
示例 5：

输入：s = "-91283472332"
输出：-2147483648
解释：
第 1 步："-91283472332"（当前没有读入字符，因为没有前导空格）
         ^
第 2 步："-91283472332"（读入 '-' 字符，所以结果应该是负数）
          ^
第 3 步："-91283472332"（读入 "91283472332"）
                     ^
解析得到整数 -91283472332 。
由于 -91283472332 小于范围 [-231, 231 - 1] 的下界，最终结果被截断为 -231 = -2147483648 。
 

提示：

0 <= s.length <= 200
s 由英文字母（大写和小写）、数字（0-9）、' '、'+'、'-' 和 '.' 组成

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnoilh/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# 比较两个无符号纯数字字符串对应的无符号整数大小，左大于右返回1，右大于左返回-1，相等返回0
def compare_num_str(s1: str, s2: str) -> int:
    s1_valid = s1.lstrip('0')
    s2_valid = s2.lstrip('0')
    n1 = len(s1_valid)
    n2 = len(s2_valid)
    if n1 == 0 or n2 == 0:
        raise ValueError('字符串长度为0')
    if n1 == n2:
        for i in range(n1):
            if ord(s1_valid[i]) < ord(s2_valid[i]):
                return -1
            elif ord(s1_valid[i]) > ord(s2_valid[i]):
                return 1
        return 0
    elif n1 > n2:
        return 1
    else:
        return -1


# 将上面的函数针对本题具体情况进行简化
def compare(s1: str, s2: str) -> int:
    s1_valid = s1.lstrip('0')
    n1 = len(s1_valid)

    if n1 < 10:
        return -1
    elif n1 > 10:
        return 1
    else:
        for i in range(n1):
            if ord(s1_valid[i]) < ord(s2[i]):
                return -1
            elif ord(s1_valid[i]) > ord(s2[i]):
                return 1
        return 0


# 传一串数字组成的字符串和一个符号标记，返回整数
# 2^31 = 2,147,483,648
# 2^31 - 1 = 2,147,483,647
def judge_and_return(s_num: str, sign: int = 1) -> int:
    if len(s_num) == 0:
        return 0
    if sign > 0:
        return 2147483647 if compare(s_num, '2147483647') > 0 else int(s_num)
    else:  # sign < 0
        return -2147483648 if compare(s_num, '2147483648') > 0 else -1 * int(s_num)


def myAtoi(s: str) -> int:
    # 将字符串左侧的连续空格剪掉
    s_valid = s.lstrip(' ')
    n = len(s_valid)

    sign = 0
    s_num = ''

    if n == 0:
        return 0

    if s_valid[0] == '+':
        sign = 1
    elif s_valid[0].isdigit():
        sign = 1
        s_num += s_valid[0]
    elif s_valid[0] == '-':
        sign = -1
    else:
        return 0

    for i in range(1, n):
        if s_valid[i].isdigit():
            s_num += s_valid[i]
        else:
            break

    return judge_and_return(s_num, sign)


if __name__ == '__main__':
    s = ''

    pprint(myAtoi(s))

    pass
