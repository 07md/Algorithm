#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time     : 2020/2/2 9:21
# @File     : BubbleSortCode.py
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> QQ        : 2426671397
# >>> Mail      : alex18812649207@gmail.com
# >>> Github    : https://github.com/koking0
# ☆ ☆ ☆ ☆ ☆ ☆ ☆


class Node:
    pass


class Union_Find_Set:

    def __init__(self):
        self.father_map = None
        self.size_map = None

    def make_sets(self, nodes):
        for node in nodes:
            self.father_map.update(node=node)
            self.size_map.update(node=1)

    def find_head(self, node: Node):
        father_node = self.father_map.get(node)
        if father_node != node:
            father_node = self.find_head(father_node)
        self.father_map.update(node=father_node)
        return father_node

    def is_same_set(self, a: Node, b: Node):
        return self.find_head(a) == self.find_head(b)

    def union(self, a: Node, b: Node):
        if a is None or b is None:
            return
        a_head = self.find_head(a)
        b_head = self.find_head(b)
        if a_head != b_head:
            a_set_size = self.size_map.get(a_head)
            b_set_size = self.size_map.get(b_head)
            if a_set_size < b_set_size:
                self.father_map.update(a_head, b_head)
                self.size_map.update(b_head, a_set_size + b_set_size)
            else:
                self.father_map.update(b_head, a_head)
                self.size_map.update(a_head, a_set_size + b_set_size)