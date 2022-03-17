# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2021.07.10 11:47
# Author  : Seto.Kaiba
from pprint import pprint
import random

"""给定一个数组 prices ，其中 prices[i] 是一支给定股票第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你可以尽可能地完成更多的交易（多次买卖一支股票）。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

 

示例 1:

输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
示例 2:

输入: prices = [1,2,3,4,5]
输出: 4
解释: 在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3:

输入: prices = [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
 

提示：

1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/top-interview-questions-easy/x2zsx1/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。"""


class Solution:
    def maxProfit(self, prices: list) -> int:
        # 只算最大利润，不给出买卖过程
        # profit = 0
        # for i in range( len(prices) - 1 ):
        #     if prices[i+1] > prices[i]:
        #         profit += prices[i+1] - prices[i]
        # return profit

        # 给出买卖过程
        profit = 0
        delta_prices = [0 for i in range(len(prices) - 1)]

        buy_day = []
        sell_day = []

        for i in range(len(prices) - 1):
            delta_prices[i] = prices[i + 1] - prices[i]

        print(prices)
        print(delta_prices)

        if delta_prices[0] > 0:
            buy_day.append(1)
            profit += delta_prices[0]

        for i in range(1, len(delta_prices)):
            if delta_prices[i] > 0 >= delta_prices[i - 1]:
                buy_day.append(i + 1)
            if delta_prices[i - 1] > 0 >= delta_prices[i]:
                sell_day.append(i + 1)
            if delta_prices[i] > 0:
                profit += delta_prices[i]

        if delta_prices[-1] > 0:
            sell_day.append(len(delta_prices) + 1)

        print("buy_day:\t{}".format(buy_day))
        print("sell_day:\t{}".format(sell_day))
        print("profit:\t{}".format(profit))


if __name__ == '__main__':
    solution = Solution()
    prices = [random.randint(1, 5) for i in range(7)]
    solution.maxProfit(prices)
    pass
