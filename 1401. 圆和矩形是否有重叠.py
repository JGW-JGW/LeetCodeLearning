# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-13 15:53
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
给你一个以 (radius, x_center, y_center) 表示的圆和一个与坐标轴平行的矩形 (x1, y1, x2, y2)，其中 (x1, y1) 是矩形左下角的坐标，(x2, y2) 是右上角的坐标。

如果圆和矩形有重叠的部分，请你返回 True ，否则返回 False 。

换句话说，请你检测是否 存在 点 (xi, yi) ，它既在圆上也在矩形上（两者都包括点落在边界上的情况）。

提示：

1 <= radius <= 2000
-10^4 <= x_center, y_center, x1, y1, x2, y2 <= 10^4
x1 < x2
y1 < y2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/circle-and-rectangle-overlapping
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

"""
矩形区域：x, y取值相互独立
两点间距离公式分别对|x - x0|, |y - y0|单调增
只要找到|x - x0|的最小值和|y - y0|的最小值即可

当x_center < x1时，min(dx) = x1 - x_center
当x1 <= x_center <= x2时，min(dx) = 0
当x_center > x2时，min(dx) = x_center - x2

当y_center < y1时，min(dy) = y1 - y_center
当y1 <= y_center <= y2时，min(dy) = 0
当y_center > y2时，min(dy) = y_center - y2
"""


class Solution:
    @staticmethod
    def checkOverlap(radius: int, x_center: int, y_center: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        if x_center < x1:
            dx = x1 - x_center
        elif x_center > x2:
            dx = x_center - x2
        else:
            dx = 0

        if y_center < y1:
            dy = y1 - y_center
        elif y_center > y2:
            dy = y_center - y2
        else:
            dy = 0

        return dx * dx + dy * dy <= radius * radius


if __name__ == '__main__':
    pass
