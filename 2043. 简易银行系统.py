# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Time    : 2022-03-18 09:13
# Author  : Seto.Kaiba
from pprint import pprint
from typing import List, Dict
import random as rd
import math
import datetime as dt
import re
from abc import ABCMeta, abstractmethod

"""
你的任务是为一个很受欢迎的银行设计一款程序，以自动化执行所有传入的交易（转账，存款和取款）。银行共有 n 个账户，编号从 1 到 n 。每个账号的初始余额存储在一个下标从 0 开始的整数数组 balance 中，其中第 (i + 1) 个账户的初始余额是 balance[i] 。

请你执行所有 有效的 交易。如果满足下面全部条件，则交易 有效 ：

指定的账户数量在 1 和 n 之间，且
取款或者转账需要的钱的总数 小于或者等于 账户余额。
实现 Bank 类：

Bank(long[] balance) 使用下标从 0 开始的整数数组 balance 初始化该对象。
boolean transfer(int account1, int account2, long money) 从编号为 account1 的账户向编号为 account2 的账户转帐 money 美元。如果交易成功，返回 true ，否则，返回 false 。
boolean deposit(int account, long money) 向编号为 account 的账户存款 money 美元。如果交易成功，返回 true ；否则，返回 false 。
boolean withdraw(int account, long money) 从编号为 account 的账户取款 money 美元。如果交易成功，返回 true ；否则，返回 false 。

提示：

n == balance.length
1 <= n, account, account1, account2 <= 10^5
0 <= balance[i], money <= 10^12
transfer, deposit, withdraw 三个函数，每个 最多调用 10^4 次

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/simple-bank-system
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Bank:
    def __init__(self, balance: List[int]):
        self.balance = [-1]
        self.balance.extend(balance)
        self.n = len(balance)

    def is_valid_account(self, account: int) -> bool:
        return 1 <= account <= self.n

    # 从编号为 account1 的账户向编号为 account2 的账户转帐 money 美元。如果交易成功，返回 true ，否则，返回 false
    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if not self.is_valid_account(account1) or not self.is_valid_account(account2) or money > self.balance[account1]:
            return False

        if account1 == account2:
            return True

        self.balance[account1] -= money
        self.balance[account2] += money

        return True

    # 向编号为 account 的账户存款 money 美元。如果交易成功，返回 true ；否则，返回 false
    def deposit(self, account: int, money: int) -> bool:
        if not self.is_valid_account(account):
            return False

        self.balance[account] += money

        return True

    # 从编号为 account 的账户取款 money 美元。如果交易成功，返回 true ；否则，返回 false
    def withdraw(self, account: int, money: int) -> bool:
        if not self.is_valid_account(account) or money > self.balance[account]:
            return False

        self.balance[account] -= money

        return True


if __name__ == '__main__':
    pass
