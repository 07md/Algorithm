#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/20 8:29
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


def check(num):
	strNumList = list(str(num))
	if '2' in strNumList or '0' in strNumList or '1' in strNumList or '9' in strNumList:
		return True
	return False


if __name__ == '__main__':
	n, ans = int(input()), 0
	for i in range(1, n + 1):
		if check(i):
			ans += i
	print(ans)
