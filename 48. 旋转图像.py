# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.12 21:47
# Author  : Seto.Kaiba
from pprint import pprint
from typing import *
import random
import math

"""
给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

 

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[[7,4,1],[8,5,2],[9,6,3]]
示例 2：


输入：matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
输出：[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
示例 3：

输入：matrix = [[1]]
输出：[[1]]
示例 4：

输入：matrix = [[1,2],[3,4]]
输出：[[3,1],[4,2]]
 

提示：

matrix.length == n
matrix[i].length == n
1 <= n <= 20
-1000 <= matrix[i][j] <= 1000

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/xnhhkv/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""


def rotate(matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    n = len(matrix)

    for circle in range(int(n / 2)):
        for j in range(circle, n - 1 - circle):
            matrix[j][n - 1 - circle], matrix[n - 1 - circle][n - 1 - j], matrix[n - 1 - j][circle], matrix[circle][j] = \
            matrix[circle][j], matrix[j][n - 1 - circle], matrix[n - 1 - circle][n - 1 - j], matrix[n - 1 - j][circle]


if __name__ == '__main__':
    n = random.randint(1, 20)
    matrix = []

    for i in range(n):
        matrix.append([random.randint(-1000, 1000) for j in range(n)])

    for item in matrix:
        for number in item:
            print("{:5d} ".format(number), end='')
        print()

    rotate(matrix)

    print("================================")

    for item in matrix:
        for number in item:
            print("{:5d} ".format(number), end='')
        print()

    pass
