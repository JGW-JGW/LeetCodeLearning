#!/usr/bin/bash
# -*- coding: utf-8 -*-
# Time    : 2022-02-26 09:54
# Author  : Seto.Kaiba

#给定一个包含电话号码列表（一行一个电话号码）的文本文件 file.txt，写一个单行 bash 脚本输出所有有效的电话号码。
#
#你可以假设一个有效的电话号码必须满足以下两种格式： (xxx) xxx-xxxx 或 xxx-xxx-xxxx。（x 表示一个数字）
#
#你也可以假设每行前后没有多余的空格字符。
#
#来源：力扣（LeetCode）
#链接：https://leetcode-cn.com/problems/valid-phone-numbers
#著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

grep -E "^[0-9]{3}-[0-9]{3}-[0-9]{4}$|^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$" file.txt
