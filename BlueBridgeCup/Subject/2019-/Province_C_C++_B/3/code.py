#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/18 11:20
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
if __name__ == '__main__':
	n1, n2, n3 = 1, 1, 1
	for i in range(6730107):
		n1 = (n1 + n2 + n3) % 10000
		n2 = (n1 + n2 + n3) % 10000
		n3 = (n1 + n2 + n3) % 10000
		if (i + 1) * 3 + 1 > 20190320:
			print(f'i = {(i + 1) * 3 + 1},', n1)
			print(f'i = {(i + 1) * 3 + 2},', n2)
			print(f'i = {(i + 1) * 3 + 3},', n3)
