#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/18 18:36
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import copy
import random


def radixSort(array: list):
	length, maxNumber, base = len(array), max(array), 0
	while 10 ** base <= maxNumber:
		buckets = [[] for _ in range(10)]
		for value in array:
			buckets[(value // 10 ** base) % 10].append(value)
		array.clear()
		for bucket in buckets:
			array.extend(bucket)
		base += 1


if __name__ == '__main__':
	flag = True
	for i in range(100):
		list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
		list2 = copy.deepcopy(list1)
		list3 = copy.deepcopy(list1)
		radixSort(list2)
		list3.sort()
		if list2 != list3:
			flag = False
			print(list1)
			print(list2)
			print(list3)
			break
	print("Nice" if flag else "Fuck")
