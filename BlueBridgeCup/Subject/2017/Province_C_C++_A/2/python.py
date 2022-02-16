# -*- coding: utf-8 -*-
# @Time        : 2022/2/14 8:45
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
from collections import deque


def bfs():
	queue = deque()
	queue.append((source, 0))
	while queue:
		front = queue.popleft()
		item, cnt = front

		if item == target:
			print(cnt)
			return

		if item in states:
			continue
		states.add(item)

		x = item.index('0')  # 空盘位置
		item = list(item)
		for dx in [2, 1, -1, -2]:
			nx = (x + dx) % 9
			item[x], item[nx] = item[nx], item[x]
			new = ''.join(item)
			if new not in states:
				queue.append((''.join(item), cnt + 1))
			item[x], item[nx] = item[nx], item[x]   # 跳完之后要恢复之前的状态再做尝试


if __name__ == '__main__':
	source = "012345678"
	target = "087654321"
	states = set()

	bfs()
