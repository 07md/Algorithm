#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/8/10 8:49
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
	ans = 0
	for i in range(1, 2020):
		if '9' in list(str(i)):
			ans += 1
	print(ans)
