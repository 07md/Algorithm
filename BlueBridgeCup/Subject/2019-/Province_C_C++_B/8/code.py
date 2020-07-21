#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/21 10:04
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


def gcd(a, b):
	return gcd(b, a % b) if b else a


if __name__ == '__main__':
	N = int(input())
	A = list(map(int, input().split(' ')))
	A.sort()
	diff = [A[i] - A[i - 1] for i in range(1, len(A))]
	ans = gcd(diff[0], diff[1])
	for i in range(2, len(diff)):
		ans = gcd(ans, diff[i])
	print(((A[-1] - A[0]) // ans) + 1 if ans else N)
