# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-28 22:01
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    @staticmethod
    def get_up_side_list(matrix: List[List[int]]) -> List[int]:
        res = matrix[0]
        del matrix[0]

        return res

    @staticmethod
    def get_right_side_list(matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        res = []
        for i in range(m):
            res.append(matrix[i][-1])
            del matrix[i][-1]

        return res

    @staticmethod
    def get_down_side_list(matrix: List[List[int]]) -> List[int]:
        res = matrix[-1]
        del matrix[-1]
        res.reverse()

        return res

    @staticmethod
    def get_left_side_list(matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        res = []
        for i in range(m - 1, -1, -1):
            res.append(matrix[i][0])
            del matrix[i][0]

        return res

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        while True:
            res += self.get_up_side_list(matrix)
            if len(matrix) == 0 or len(matrix[0]) == 0:
                break
            res += self.get_right_side_list(matrix)
            if len(matrix) == 0 or len(matrix[0]) == 0:
                break
            res += self.get_down_side_list(matrix)
            if len(matrix) == 0 or len(matrix[0]) == 0:
                break
            res += self.get_left_side_list(matrix)
            if len(matrix) == 0 or len(matrix[0]) == 0:
                break

        return res


"""
真删肯定不如假删快

 1. 设定上下左右边界
 2. 向右取出第一行，可将第一行从矩阵中删除，体现在代码中就是重新定义上边界
 3. 若重新定义上边界后，上下边界交错，表明遍历结束，可以返回答案
 4. 向下取出最后一列，可将最后一列从矩阵中删除，体现在代码中就是重新定义右边界
 5. 若重新定义右边界后，左右边界交错，表明遍历结束，可以返回答案
 6. 向左取出最后一行，可将最后一行从矩阵中删除，体现在代码中就是重新定义下边界
 7. 若重新定义下边界后，上下边界交错，表明遍历结束，可以返回答案
 8. 向上取出第一列，可将第一列从矩阵中删除，体现在代码中就是重新定义左边界
 9. 若重新定义左边界后，左右边界交错，表明遍历结束，可以返回答案
10. 重复 2 ~ 9，直至返回答案
"""


class Solution:
    @staticmethod
    def spiralOrder(matrix: List[List[int]]) -> List[int]:
        res = []
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return res

        # 初始化上下左右边界
        u = 0
        d = m - 1
        l = 0
        r = n - 1

        while True:
            for i in range(l, r + 1):
                res.append(matrix[u][i])
            u += 1
            if u > d:
                break

            for i in range(u, d + 1):
                res.append(matrix[i][r])
            r -= 1
            if r < l:
                break

            for i in range(r, l - 1, -1):
                res.append(matrix[d][i])
            d -= 1
            if d < u:
                break

            for i in range(d, u - 1, -1):
                res.append(matrix[i][l])
            l += 1
            if l > r:
                break

        return res


if __name__ == '__main__':
    s = Solution()

    il = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
        [[7], [9], [6]],
    ]

    for matrix in il:
        pprint(s.spiralOrder(matrix))
    pass
