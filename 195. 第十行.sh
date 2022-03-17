#!/usr/bin/env bash
# -*- coding: utf-8 -*-
# Time    : 2022-03-08 21:43
# Author  : Seto.Kaiba

# 给定一个文本文件 file.txt，请只打印这个文件中的第十行。

# awk较慢
awk 'NR==10' file.txt

# sed最快
sed -n 10p file.txt

# tail + head较慢
tail -n +10 file.txt | head -1
