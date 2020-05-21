#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/5/21 21:45
# @File     : 5. Longest Palindromic Substring.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Solution:
	def longestPalindrome_violence(self, s: str) -> str:
		if len(s) == 1:
			return s

		for i in range(int(len(s) / 2)):
			if s[i] != s[len(s) - i - 1]:
				break
		else:
			return s

		substring = ""

		for i in range(len(s)):
			for j in range(i + 1, len(s) + 1):
				substring_temp = s[i:j]
				substring_length = len(substring_temp)

				for k in range(int(1 + substring_length / 2)):
					if substring_temp[k] != substring_temp[substring_length - k - 1]:
						break
				else:
					if substring_length > len(substring):
						substring = substring_temp
		return substring

	def longestPalindrome_manacher(self, s: str) -> str:
		def expand(s, left, right):
			while left > -1 and right < len(s) and s[left] == s[right]:
				left -= 1
				right += 1
			return (right - left - 2) // 2

		end, start = -1, 0
		s = '#' + '#'.join(list(s)) + '#'
		arm_len = []
		right = -1
		j = -1
		for i in range(len(s)):
			if right >= i:
				i_sym = 2 * j - i
				min_arm_len = min(arm_len[i_sym], right - i)
				cur_arm_len = expand(s, i - min_arm_len, i + min_arm_len)
			else:
				cur_arm_len = expand(s, i, i)
			arm_len.append(cur_arm_len)
			if i + cur_arm_len > right:
				j = i
				right = i + cur_arm_len
			if 2 * cur_arm_len + 1 > end - start:
				start = i - cur_arm_len
				end = i + cur_arm_len
		return s[start + 1:end + 1:2]
