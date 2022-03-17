# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-02-24 10:28
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict, Tuple
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
用一个大小为 m x n 的二维网格 grid 表示一个箱子。你有 n 颗球。箱子的顶部和底部都是开着的。

箱子中的每个单元格都有一个对角线挡板，跨过单元格的两个角，可以将球导向左侧或者右侧。

将球导向右侧的挡板跨过左上角和右下角，在网格中用 1 表示。
将球导向左侧的挡板跨过右上角和左下角，在网格中用 -1 表示。
在箱子每一列的顶端各放一颗球。每颗球都可能卡在箱子里或从底部掉出来。如果球恰好卡在两块挡板之间的 "V" 形图案，或者被一块挡导向到箱子的任意一侧边上，就会卡住。

返回一个大小为 n 的数组 answer ，其中 answer[i] 是球放在顶部的第 i 列后从底部掉出来的那一列对应的下标，如果球卡在盒子里，则返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/where-will-the-ball-fall
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


|╲|╱|

1 |o╱|...|         最左一列，当前格子为-1，则卡住
2 |...|╲o|         最右一列，当前格子为1，则卡住
3 |╲o|╱|...|       非最右一列，当前格子为1，右侧格子为-1，则卡住
4 |╲o|╲|...|       非最右一列，当前格子为1，右侧格子为1，则到达右下方的格子
5 |...|╲|o╱|       非最左一列，当前格子为-1，左侧格子为1，则卡住
6 |...|╱|o╱|       非最左一列，当前格子为-1，左侧格子为-1，则到达左下方的格子

当到达第m+1行时，取小球所在的列作为返回值

"""


class Solution:
    @staticmethod
    def get_next_position(coordinate: Tuple[int, int], grid: List[List[int]]) -> Tuple[int, int] or None:
        n = len(grid[0])
        x, y = coordinate
        if y == 0 and grid[x][y] == -1:
            return None
        elif y == n - 1 and grid[x][y] == 1:
            return None
        elif y < n - 1 and grid[x][y] == 1 and grid[x][y + 1] == -1:
            return None
        elif y < n - 1 and grid[x][y] == 1 and grid[x][y + 1] == 1:
            return x + 1, y + 1
        elif y > 0 and grid[x][y] == -1 and grid[x][y - 1] == 1:
            return None
        elif y > 0 and grid[x][y] == -1 and grid[x][y - 1] == -1:
            return x + 1, y - 1
        else:
            raise ValueError('WTF')

    def findBall(self, grid: List[List[int]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])
        result_list = [-1 for _ in range(n)]
        x_list = [0 for _ in range(n)]  # balls' init row number
        y_list = [i for i in range(n)]  # balls' init col number
        for i in range(n):
            coordinate = (x_list[i], y_list[i])
            while coordinate[0] < m:
                coordinate_next = self.get_next_position(coordinate, grid)
                if coordinate_next is not None:
                    coordinate = coordinate_next
                    continue
                else:
                    coordinate = None
                    break
            if coordinate is None:
                continue
            else:
                result_list[i] = coordinate[1]

        return result_list


"""
我们依次判断每个球的最终位置。对于每个球，从上至下判断球位置的移动方向。

在对应的位置，如果挡板向右偏，则球会往右移动；如果挡板往左偏，则球会往左移动。

若移动过程中碰到侧边或者 V 型，则球会停止移动，卡在箱子里。

如果可以完成本层的移动，则继续判断下一层的移动方向，直到落出箱子或者卡住。
"""


class Solution1(object):
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n = len(grid[0])
        result_list = [-1 for _ in range(n)]
        for j in range(n):
            col = j  # 球的初始列数
            for row in grid:
                direction = row[col]  # 1表示球会向右下移动，-1表示向左下移动
                col += direction  # 移动后的列数
                if col < 0 or col == n or row[col] != direction:  # 到达两边或遇到V型
                    break
            else:  # 执行完毕没有break
                result_list[j] = col
        return result_list


if __name__ == '__main__':
    s = Solution()
    grid_list = [
        [[1, 1, -1]],
        [[1, 1, 1, -1, -1], [1, 1, 1, -1, -1], [-1, -1, -1, 1, 1], [1, 1, 1, 1, -1], [-1, -1, -1, -1, -1]]
    ]
    for grid in grid_list:
        pprint(s.findBall(grid))
    pass
