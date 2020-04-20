#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/4/21 0:06
# @File     : code.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex 007
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


def LCS(A: str, B: str):
    lengthA, lengthB = len(A), len(B)
    dp = [[0 for _ in range(lengthA)] for _ in range(lengthB)]
    for i in range(lengthA):
        if A[i] == B[0]:
            dp[i][0] = 1
            for j in range(i + 1, lengthB):
                dp[j][0] = 1
            break
    for i in range(lengthB):
        if B[i] == A[0]:
            dp[0][i] = 1
            for j in range(i + 1, lengthB):
                dp[0][j] = 1
            break
    for i in range(1, lengthA):
        for j in range(1, lengthB):
            if A[i] == B[j]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    for i in range(lengthA):
        for j in range(lengthB):
            print(dp[i][j], end=" ")
        print()
    return dp[lengthA - 1][lengthB - 1]


if __name__ == '__main__':
    LCS("android", "random")
