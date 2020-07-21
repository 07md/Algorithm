#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/17 9:23
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
	ans, team = 0, [[1, 97, 90, 0, 0, 0],
	                [2, 92, 85, 96, 0, 0],
	                [3, 0, 0, 0, 0, 93],
	                [4, 0, 0, 0, 80, 86],
	                [5, 89, 83, 97, 0, 0],
	                [6, 82, 86, 0, 0, 0],
	                [7, 0, 0, 0, 87, 90],
	                [8, 0, 97, 96, 0, 0],
	                [9, 0, 0, 89, 0, 0],
	                [10, 95, 99, 0, 0, 0],
	                [11, 0, 0, 96, 97, 0],
	                [12, 0, 0, 0, 93, 98],
	                [13, 94, 91, 0, 0, 0],
	                [14, 0, 83, 87, 0, 0],
	                [15, 0, 0, 98, 97, 98],
	                [16, 0, 0, 0, 93, 86],
	                [17, 98, 83, 99, 98, 81],
	                [18, 93, 87, 92, 96, 98],
	                [19, 0, 0, 0, 89, 92],
	                [20, 0, 99, 96, 95, 81]]
	for i in range(20):
		if team[i][1]:
			for j in range(20):
				if j != i:
					for k in range(20):
						if k != i and k != j:
							for m in range(20):
								if m != i and m != j and m != k:
									for n in range(20):
										if n != i and n != j and n != k and n != m:
											ans = max(ans, team[i][1] + team[j][2] + team[k][3] + team[m][4] + team[n][5])
	print(ans)
