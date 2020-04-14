#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/14 11:52
# @File     : 01.Hanoi.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://blog.csdn.net/weixin_43336281
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def hanoi(n, start, helper, target):
    """
    :param n: 表示盘子的个数
    :param start: 表示起始柱子
    :param helper: 表示辅助柱子
    :param target: 表示目标柱子
    """
    if n > 0:
        hanoi(n - 1, start, target, helper)
        print(f"Move {n} from {start} to {target}")
        hanoi(n - 1, helper, start, target)


if __name__ == '__main__':
    hanoi(3, "A", "B", "C")
