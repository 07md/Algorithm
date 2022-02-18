# -*- coding: utf-8 -*-
# @Time        : 2022/2/18 8:57
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
	ans = 0
	for i in range(1, 100):
		if sum(map(int, list(str(i ** 3)))) == i:
			ans += 1
	print(ans)
