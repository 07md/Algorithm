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
	answer = [[0 for _ in range(nums)] for _ in range(floors)]
	# 2.填充第一列
	for t in range(floors):
		answer[t][0] = t + 1
	# 3.填充第一行
	for n in range(nums):
		answer[0][n] = 1
	# 4.根据公式求解其它值
	for t in range(1, floors):
		for n in range(1, nums):
			minNum = sys.maxsize
			for k in range(1, t + 1):
				minNum = min(minNum, 1 + max(answer[k - 1][n - 1], answer[t - k - 1][n]))
			answer[t][n] = minNum
	return answer


if __name__ == '__main__':
	m = solve(10, 10)
	for floor in range(10):
		print(f"Floor = {floor}:\t", end="")
		for num in range(10):
			print(m[floor][num], end="\t")
		print()
