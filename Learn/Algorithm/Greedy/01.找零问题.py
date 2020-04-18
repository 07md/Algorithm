#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/16 8:12
# @File     : 01.找零问题.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# 假设商店老板需要找零 n 元钱，钱币的面额有：100元、50元、20元、5元、1元，如何找零使得所需钱币的数量最少？


def changeMoney(Denomination: list, amountOfMoney: int):
	"""
	:param Denomination: 钱币的所有面额
	:param amountOfMoney: 找零的目标金额
	:return: 不同面额钱币的张数和找不开的金额
	"""
	count = [0 for _ in range(len(Denomination))]
	for index, value in enumerate(Denomination):
		count[index] = amountOfMoney // Denomination[index]
		amountOfMoney %= Denomination[index]
	return count, amountOfMoney


if __name__ == '__main__':
	print(changeMoney([100, 50, 20, 5, 1], 376))
