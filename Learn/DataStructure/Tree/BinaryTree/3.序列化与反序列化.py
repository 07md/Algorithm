#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/27 19:43
# @File     : 3.序列化与反序列化.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from collections import deque


class Node:
	def __init__(self, value=None):
		self.value, self.left, self.right = value, None, None

	def preSerial(self):
		if self is None:
			return "#!"
		string = str(self.value) + "!"
		string += Node.preSerial(self.left)
		string += Node.preSerial(self.right)
		return string

	@staticmethod
	def preStringDeserialization(string):
		values, queue = string.split("!"), deque()
		for value in values:
			queue.append(value)
		return Node.preDeserialization(queue)

	@staticmethod
	def preDeserialization(queue):
		if queue:
			value = queue.popleft()
			if value == "#":
				return
			temp = Node(value)
			temp.left = Node.preDeserialization(queue)
			temp.right = Node.preDeserialization(queue)
			return temp

	def inOrderRecursive(self):
		if self is None:
			return
		if self.left:
			self.left.inOrderRecursive()
		print(self.value, end=' ')
		if self.right:
			self.right.inOrderRecursive()


if __name__ == '__main__':
	node = Node.preStringDeserialization("1!2!4!#!#!5!#!#!3!6!#!#!7!#!#!")
	print(node.inOrderRecursive())
