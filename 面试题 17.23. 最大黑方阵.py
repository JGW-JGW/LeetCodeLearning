# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-18 09:45
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict, Tuple
import random as rd
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给定一个方阵，其中每个单元(像素)非黑即白。设计一个算法，找出 4 条边皆为黑色像素的最大子方阵。

返回一个数组 [r, c, size] ，其中 r, c 分别代表子方阵左上角的行号和列号，size 是子方阵的边长。若有多个满足条件的子方阵，返回 r 最小的，若 r 相同，返回 c 最小的子方阵。若无满足条件的子方阵，返回空数组。

提示：

matrix.length == matrix[0].length <= 200

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/max-black-square-lcci
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    # 判断以 (r, c) 为左上角，且边长为 a 的正方形的四边是否都是黑色
    @staticmethod
    def is_square(matrix: List[List[int]], n: int, r: int, c: int, a: int) -> bool:
        if a == 1:
            return not matrix[r][c]

        if n - r < a or n - c < a:
            return False

        # 上边 和 下边
        for i in range(c, c + a):
            if matrix[r][i] or matrix[r + a - 1][i]:
                return False

        # 左边 和 右边
        for i in range(r + 1, r + a - 1):
            if matrix[i][c] or matrix[i][c + a - 1]:
                return False

        return True

    # 给定边长 a，给定行标 r，求该行从左到右第一组连续出现 a + 1 个 0 的起点列标 col_start
    @staticmethod
    def find_col_start_of_row(matrix: List[List[int]], n: int, r: int, a: int) -> int:
        col = 0
        length = 0
        while col < n:
            if matrix[r][col] == 1:
                length = 0
                col += 1
                continue

            # 找到了 0
            length += 1
            if length > a:
                return col - length + 1
            col += 1

        return -1

    # 寻找某一行最大的且最靠左的正方形 与 当前全局最大正方形 的比较结果
    # 假设当前已经知道了目前为止已经找到的最大正方形
    def find_max_square_of_row(self, matrix: List[List[int]], n: int, r: int, max_of_all: Tuple[int, int, int]) -> Tuple[int, int, int]:
        r_max, c_max, a_max = max_of_all
        col_start = self.find_col_start_of_row(matrix, n, r, a_max)

        # 如果没能找到更长的连续的 0，或者纵向行数跨度不足，则直接返回全局最大
        if col_start == -1 or n - r <= a_max:
            return max_of_all

        # 只判断边长大于 a_max 的情况，边长最小可以取 a_max + 1，最大可以取 n - col_start
        for a in range(n - col_start, a_max, -1):
            # 第一条满足长度的边 列起点：col_start 列终点：col_start + a - 1
            # 最后一条满足长度的边 列终点：n - 1 列起点：n - a
            for c in range(col_start, n - a + 1):
                if self.is_square(matrix, n, r, c, a):
                    return r, c, a

        return max_of_all

    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        max_of_all = (-1, -1, 0)

        # 先找到一个 0
        r = 0
        while r < n and max_of_all[2] == 0:
            c = 0
            while c < n and max_of_all[2] == 0:
                if matrix[r][c] == 0:
                    max_of_all = (r, c, 1)
                c += 1
            r += 1

        if max_of_all[2] == 0:
            return []

        for r in range(max_of_all[0], n):
            max_of_all = self.find_max_square_of_row(
                matrix=matrix,
                n=n,
                r=r,
                max_of_all=max_of_all
            )

        return list(max_of_all)


"""
重构矩阵 rightward_continuous_zero_matrix 和 downward_continuous_zero_matrix
rightward_continuous_zero_matrix[r][c] 表示 matrix[r][c] 从自身开始向右有多少个连续的 0
downward_continuous_zero_matrix[r][c] 表示 matrix[r][c] 从自身开始向下有多少个连续的 0

记 rightward_continuous_zero_matrix 为 rczm
记 downward_continuous_zero_matrix 为 dczm


对于给定的行标列标 (r, c)，能组成的最大边长为 min(rczm[r][c], dczm[r][c]
对于给定的行标列标 (r, c) 和边长 a，能够组成正方形的条件为
dczm[r][c + a - 1] >= a 且 rczm[r + a - 1][c] >= a
"""


class Solution(object):
    @staticmethod
    def cal_rczm(matrix: List[List[int]], n: int, rczm: List[List[int]]) -> None:
        for r in range(n - 1, -1, -1):
            count = 0
            for c in range(n - 1, -1, -1):
                if matrix[r][c] == 1:
                    count = 0
                else:
                    count += 1

                rczm[r][c] = count

        return

    @staticmethod
    def cal_dczm(matrix: List[List[int]], n: int, dczm: List[List[int]]) -> None:
        for c in range(n - 1, -1, -1):
            count = 0
            for r in range(n - 1, -1, -1):
                if matrix[r][c] == 1:
                    count = 0
                else:
                    count += 1

                dczm[r][c] = count

        return

    @staticmethod
    def is_valid_square(rczm: List[List[int]], dczm: List[List[int]], n: int, r: int, c: int, a: int) -> bool:
        if r + a - 1 >= n or c + a - 1 >= n:
            return False

        if rczm[r + a - 1][c] >= a and dczm[r][c + a - 1] >= a:
            return True

        return False

    def findSquare(self, matrix: List[List[int]]) -> List[int]:
        n = len(matrix)
        rczm = [[0 for _ in range(n)] for _ in range(n)]
        dczm = [[0 for _ in range(n)] for _ in range(n)]
        max_of_all = (-1, -1, 0)

        self.cal_rczm(matrix, n, rczm)
        self.cal_dczm(matrix, n, dczm)

        for r in range(n):
            for c in range(n):
                max_a = min(rczm[r][c], dczm[r][c])

                while max_a > 0:
                    if self.is_valid_square(rczm, dczm, n, r, c, max_a):
                        break
                    max_a -= 1

                if max_a > max_of_all[2]:
                    max_of_all = (r, c, max_a)

        return list(max_of_all) if max_of_all[2] > 0 else []


if __name__ == '__main__':
    s = Solution()

    il = [
        [
            [1, 1, 1, 1],
            [1, 0, 1, 1],
            [1, 0, 0, 0],
            [1, 0, 0, 0],
        ],
        [
            [1, 0, 1],
            [0, 0, 1],
            [0, 0, 1]
        ],
        [
            [0, 1, 1],
            [1, 0, 1],
            [1, 1, 0]
        ],
        [[1]],
        [
            [1, 1, 1, 0, 1, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 1, 0, 0, 0, 1, 1],
            [0, 0, 1, 1, 0, 0, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 1, 0, 0, 1],
            [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 1, 1, 1],
            [1, 0, 1, 0, 1, 0, 0, 0, 1, 0],
            [1, 1, 1, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0]
        ],
        [
            [1, 1, 0, 0, 1, 1, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 1, 1, 0, 0, 1, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
            [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 1, 1, 0, 1, 1],
            [0, 0, 1, 1, 1, 1, 0, 1, 0, 1],
            [1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
            [1, 0, 1, 0, 1, 0, 0, 0, 1, 1]
        ],
    ]

    for matrix in il:
        pprint(s.findSquare(matrix))
        # pprint(s.find_col_start_of_row(matrix, len(matrix), 1, 3))
        # pprint(s.find_max_square_of_row(matrix, len(matrix), 2, (1, 1, 1)))
    pass
