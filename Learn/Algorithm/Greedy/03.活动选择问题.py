#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/16 9:09
# @File     : 03.活动选择问题.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def activitySelection(activities: list):
	activities.sort(key=lambda x: x[1])
	result = [activities[0]]
	for index in range(1, len(activities)):
		if activities[index][0] >= result[-1][1]:
			result.append(activities[index])
	return result


if __name__ == '__main__':
	print(activitySelection([(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (12, 16)]))
