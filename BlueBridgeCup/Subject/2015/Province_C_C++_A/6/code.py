#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/3/11 16:11
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://blog.csdn.net/weixin_43336281
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
"""
牌型：   A   2   3   4   5   6   7   8   9   10  J   Q   K   A
转换：   0   1   2   3   4   5   6   7   8   9   10  11  12  13
数量：	0   0   0   0   0   0   0   0   0   0   0   0   0   0
		1   1   1   1   1   1   1   1   1   1   1   1   1   1
		2   2   2   2   2   2   2   2   2   2   2   2   2   2
		3   3   3   3   3   3   3   3   3   3   3   3   3   3
		4   4   4   4   4   4   4   4   4   4   4   4   4   4
5 ** 13 = 1,220,703,125
"""
answer = 0


def dfs(count, index):
	"""
	:param count:表示现在手里的牌数
	:param index:表示当前判断的牌型
	:return:
	"""
	if count > 13 or index > 13:
		return
	if count == 13 and index == 13:
		global answer
		answer += 1
	for i in range(5):
		dfs(count+i, index + 1)


if __name__ == '__main__':
	dfs(0, 0)
	print(answer)
