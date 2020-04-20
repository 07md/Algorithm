#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/20 23:27
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import sys


def solve(floors, nums):
	# 1.创建DP数组
	answer = [[sys.maxsize for _ in range(nums + 1)] for _ in range(floors + 1)]
	# 2.填充第一列
	for t in range(1, floors + 1):
		answer[t][1] = t
	# 3.填充第一行
	for n in range(nums + 1):
		answer[1][n] = 1
	# 4.根据公式求解其它值
	for t in range(2, floors + 1):
		for n in range(2, nums + 1):
			minNum = sys.maxsize
			for k in range(1, floors + 1):
				if t > k:
					minNum = min(minNum, 1 + max(answer[k - 1][n - 1], answer[t - k][n]))
			answer[t][n] = minNum
	return answer


if __name__ == '__main__':
	m = solve(10, 10)
	for floor in range(1, 11):
		print(f"Floor = {floor}:\t", end="")
		for num in range(1, 11):
			print(m[floor][num], end="\t")
		print()
