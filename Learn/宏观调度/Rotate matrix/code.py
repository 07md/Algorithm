#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/1/20 上午10:10
# @File     : BubbleSortCode.py
# @Project  : Algorithm
# @Software : PyCharm
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 


def rotate_edge(input_matrix, left_row, left_col, right_row, right_co1):
    for index in range(right_co1 - left_col):
        [input_matrix[left_row][left_col + index], input_matrix[right_row - index][left_col],
         input_matrix[right_row][right_co1 - index], input_matrix[left_row + index][right_co1]] \
            = [input_matrix[right_row - index][left_col], input_matrix[right_row][right_co1 - index],
               input_matrix[left_row + index][right_co1], input_matrix[left_row][left_col + index]]


def rotate_matrix(input_matrix):
    left_row, left_col, right_row, right_col = 0, 0, len(input_matrix) - 1, len(input_matrix[0]) - 1
    while left_row <= right_row and left_col <= right_col:
        rotate_edge(input_matrix, left_row, left_col, right_row, right_col)
        left_row += 1
        left_col += 1
        right_row -= 1
        right_col -= 1


if __name__ == '__main__':
    matrix = [[1, 2, 3, 4],
              [5, 6, 7, 8],
              [9, 10, 11, 12],
              [13, 14, 15, 16]]
    for i in matrix:
        print(i)
    print('-----------')
    rotate_matrix(matrix)
    for i in matrix:
        print(i)
