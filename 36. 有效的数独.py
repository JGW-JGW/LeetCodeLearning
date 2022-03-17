# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.11 21:40
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
请你判断一个 9x9 的数独是否有效。只需要 根据以下规则 ，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。（请参考示例图）
数独部分空格内已填入了数字，空白格用 '.' 表示。

注意：

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
 

示例 1：


输入：board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：true
示例 2：

输入：board = 
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
输出：false
解释：除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。 但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
 

提示：

board.length == 9
board[i].length == 9
board[i][j] 是一位数字或者 '.'

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2f9gg/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


# 判断一个列表是否含有相同的数字
def contains_duplicate_numbers(input_list: List[str]):
    # 手动建集合
    temp_set = set()
    for i in range(len(input_list)):
        if input_list[i].isdigit():
            if input_list[i] in temp_set:
                return True
            else:
                temp_set.add(input_list[i])
    return False


def isValidSudoku(board: List[List[str]]) -> bool:
    # 自己想的方法，想办法把每组9个数字都挖出来然后判断是否合适
    # for i in range(9):
    #     if contains_duplicate_numbers(board[i]):
    #         return False
    #
    # # j是列标，i为行标，提取竖向的列表
    # for j in range(9):
    #     temp_list_vertical = []
    #     for i in range(9):
    #         temp_list_vertical.append(board[i][j])
    #     if contains_duplicate_numbers(temp_list_vertical):
    #         return False
    #
    #
    # # 提取块状9格
    # for i in range(3):
    #     for j in range(3):
    #         temp_list_block = []
    #         for row_index in range(3*i, 3*i+3):
    #             for col_index in range(3*j, 3*j+3):
    #                 temp_list_block.append(board[row_index][col_index])
    #         if contains_duplicate_numbers(temp_list_block):
    #             return False
    #
    # return True

    # 改进：在添加过程中直接判定，并且更方便地提取块状9个数字
    for i in range(9):
        set_horizontal = set()
        set_vertical = set()
        set_block = set()
        for j in range(9):
            if board[i][j].isdigit() and board[i][j] in set_horizontal:
                return False
            else:
                set_horizontal.add(board[i][j])

            if board[j][i].isdigit() and board[j][i] in set_vertical:
                return False
            else:
                set_vertical.add(board[j][i])

            row_index = int(i / 3) * 3 + int(j / 3)
            col_index = int(i % 3) * 3 + int(j % 3)
            if board[row_index][col_index].isdigit() and board[row_index][col_index] in set_block:
                return False
            else:
                set_block.add(board[row_index][col_index])
    return True


if __name__ == '__main__':
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", "4", "8", ".", ".", "7", "9"]
    ]

    pprint(isValidSudoku(board))

    pass
