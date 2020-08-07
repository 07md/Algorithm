#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/7/31 7:49
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> WeChat    : Alex-Paddle
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import datetime

if __name__ == '__main__':
	birth = datetime.datetime.strptime("1777-04-30", "%Y-%m-%d")
	new = birth + datetime.timedelta(days=8112)
	print(new)
