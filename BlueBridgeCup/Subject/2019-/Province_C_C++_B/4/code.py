#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/19 9:52
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def judge(num):
	strList = list(str(num))
	return False if '2' in strList or '4' in strList else True


if __name__ == '__main__':
	ans = 0
	for i in range(1, 2019):
		if judge(i):
			for j in range(i + 1, 2019):
				if judge(j) and (2019 - i - j) > j and judge(2019 - i - j):
					ans += 1
					print(f'ans = {ans}, {i} + {j} + {2019 - i - j} = 2019')
	print(ans)
