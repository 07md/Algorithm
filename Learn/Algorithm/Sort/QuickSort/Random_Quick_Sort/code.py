# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/14 下午9:58
# @File     : code.py
# @Project  : Algorithm
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import copy
import random


def random_quick_sort(arr: list):
    if len(arr) < 2:
        return
    randomQuickSort(arr, 0, len(arr) - 1)


def randomQuickSort(arr: list, left: int, right: int):
    if left < right:
        less, more = partition(arr, left, right, arr[random.randint(left, right)])
        randomQuickSort(arr, left, less)
        randomQuickSort(arr, more, right)


def partition(arr: list, left: int, right: int, p: int):
    less = left - 1
    more = right + 1
    while left < more:
        if arr[left] < p:
            less += 1
            arr[left], arr[less] = arr[less], arr[left]
            left += 1
        elif arr[left] > p:
            more -= 1
            arr[left], arr[more] = arr[more], arr[left]
        else:
            left += 1
    return less, more


def generate_random_test(size_max: int, value_max: int):
    result = []
    size = random.randint(0, size_max + 1)
    for temp in range(size):
        result.append((int(value_max + 1) * random.random()) - int(value_max * random.random()))
    return result


if __name__ == '__main__':
    test_num = 100
    max_size = 100
    max_value = 100
    flag = True

    for i in range(test_num):
        list1 = generate_random_test(max_size, max_value)
        list2 = copy.deepcopy(list1)
        list3 = copy.deepcopy(list1)
        random_quick_sort(list2)
        list3.sort()
        if list2 != list3:
            flag = False
            print(list1)
            print(list2)
            print(list3)
            break

    print("Nice" if flag else "Fuck")
