# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ----------------------------------------------
# >>> File Name : code.py
# >>> Created Time: 2020年01月12日 星期日 22时25分25秒
# !/usr/bin/python
# -*- coding:utf-8 -*-
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import copy
import random


def mergeSort(arr: list, left: int, right: int):
	if left == right:
		return
	mid = left + ((right - left) >> 1)
	mergeSort(arr, left, mid)
	mergeSort(arr, mid + 1, right)
	merge(arr, left, mid, right)


def merge(arr: list, left: int, mid: int, right: int):
	helpList, p1, p2 = [], left, mid + 1
	while p1 < mid + 1 and p2 < right + 1:
		if arr[p1] < arr[p2]:
			helpList.append(arr[p1])
			p1 += 1
		else:
			helpList.append(arr[p2])
			p2 += 1
	while p1 < mid + 1:
		helpList.append(arr[p1])
		p1 += 1
	while p2 < right + 1:
		helpList.append(arr[p2])
		p2 += 1
	for index in range(len(helpList)):
		arr[left + index] = helpList[index]


if __name__ == '__main__':
	flag = True
	for i in range(100):
		list1 = [random.randint(0, 100) for _ in range(random.randint(0, 100))]
		list2 = copy.deepcopy(list1)
		list3 = copy.deepcopy(list1)
		mergeSort(list2, 0, len(list2) - 1)
		list3.sort()
		if list2 != list3:
			flag = False
			print(list1)
			print(list2)
			print(list3)
			break
	print("Nice" if flag else "Fuck")
