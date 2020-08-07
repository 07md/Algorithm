#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/31 8:01
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
if __name__ == '__main__':
	for num in range(100000, 1000000):
		square = num ** 2
		if len(set(str(num))) == 6 and not (set(str(num)) & set(str(square))):
			print(f'{num} * {num} = {num ** 2}')
