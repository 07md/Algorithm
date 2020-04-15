#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/12 下午5:43
# @Author   : alex
# @File     : code.py
# @Project  : Algorithm
# @Software : PyCharm
import copy
import random


def bubbleSort(arr: list):
	length = len(arr)
	for trip in range(length):
		for index in range(length - trip - 1):
			if arr[index] > arr[index + 1]:
				arr[index], arr[index + 1] = arr[index + 1], arr[index]


if __name__ == '__main__':
	flag = True
	for i in range(100):
		list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
		list2 = copy.deepcopy(list1)
		list3 = copy.deepcopy(list1)
		bubbleSort(list2)
		list3.sort()
		if list2 != list3:
			flag = False
			print(list1)
			print(list2)
			print(list3)
			break
	print("Nice" if flag else "Fuck")
