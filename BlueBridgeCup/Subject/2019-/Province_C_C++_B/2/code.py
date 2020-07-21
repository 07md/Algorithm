#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/17 11:31
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
	num = 2019
	while num:
		print(chr(num % 26 + ord('A') - 1))
		num = num // 26
