# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-05 11:09
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
3 x 3 的幻方是一个填充有 从 1 到 9  的不同数字的 3 x 3 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。

给定一个由整数组成的row x col 的 grid，其中有多少个 3 × 3 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。

 

提示:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/magic-squares-in-grid
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
记行数为m，记列数为n
如果m或n小于3，则返回0


"""


class Solution:
    @staticmethod
    def is_a_magic_square(num1: int, num2: int, num3: int, num4: int, num5: int, num6: int, num7: int, num8: int,
                          num9: int) -> bool:
        if num5 != 5 or num1 & 1 == 1 or num3 & 1 == 1 or num7 & 1 == 1 or num9 & 1 == 1 or num1 + num9 != 10 or num3 + num7 != 10 or num2 != 15 - num1 - num3 or num4 != 15 - num1 - num7 or num6 != 15 - num3 - num9 or num8 != 15 - num7 - num9:
            return False
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        count = 0
        for m in range(row - 2):
            for n in range(col - 2):
                if self.is_a_magic_square(
                        grid[m][n],
                        grid[m][n + 1],
                        grid[m][n + 2],
                        grid[m + 1][n],
                        grid[m + 1][n + 1],
                        grid[m + 1][n + 2],
                        grid[m + 2][n],
                        grid[m + 2][n + 1],
                        grid[m + 2][n + 2]
                ):
                    count += 1

        return count


if __name__ == '__main__':
    pass
