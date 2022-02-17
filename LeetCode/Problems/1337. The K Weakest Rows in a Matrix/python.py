# -*- coding: utf-8 -*-
# @Time        : 2022/2/14 20:43
# @File        : python.py
# @Description : None
# ----------------------------------------------
# ☆ ☆ ☆ ☆ ☆ ☆ ☆ 
# >>> Author    : Alex
# >>> Mail      : liu_zhao_feng_alex@163.com
# >>> Github    : https://github.com/koking0
# >>> Blog      : https://alex007.blog.csdn.net/
# ☆ ☆ ☆ ☆ ☆ ☆ ☆
import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = [(sum(val), idx) for idx, val in enumerate(mat)]
        heapq.heapify(power)
        return [heapq.heappop(power)[1] for _ in range(k)]
