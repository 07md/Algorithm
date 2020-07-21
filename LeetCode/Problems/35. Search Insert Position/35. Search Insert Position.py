#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/17 8:43
# @File     : 35. Search Insert Position.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from typing import List


class Solution:
	def searchInsert(self, nums: List[int], target: int) -> int:
		ans, left, right = len(nums), 0, len(nums) - 1
		while left <= right:
			middle = ((right - left) >> 1) + left
			if target <= nums[middle]:
				right = middle - 1
				ans = middle
			else:
				left = middle + 1
		return ans
