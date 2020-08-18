#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/8/18 8:25
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> WeChat    : Alex-Paddle
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import itertools


if __name__ == '__main__':
	s = list("LANQIAO")
	print(len(set(itertools.permutations(s))))
