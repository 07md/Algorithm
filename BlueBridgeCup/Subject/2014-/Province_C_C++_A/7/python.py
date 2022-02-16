# -*- coding: utf-8 -*-
# @Time        : 2022/2/15 8:59
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
if __name__ == '__main__':
	n = int(input())
	left, right = 0, 0
	nums = list(map(int, input().split()))
	for val in nums:
		if abs(val) > abs(nums[0]) and val < 0:
			right += 1
		if abs(val) < abs(nums[0]) and val > 0:
			left += 1
	if (nums[0] > 0 and right == 0) or (nums[0] < 0 and left == 0):
		print(1)
	else:
		print(left + right + 1)
