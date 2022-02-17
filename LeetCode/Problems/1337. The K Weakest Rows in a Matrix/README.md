[1337. 矩阵中战斗力最弱的 K 行](https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix/)

## Ideas

Top K 问题一般都是通过堆来解决，这道题要求的是最弱的 K 行，说明这是一个小根堆问题。

题目中是根据军人的数量来衡量战斗力的，而军人的数量其实就是当前行的列表求和，所以我们可以将（当前行列表求和，行索引）构造一个小根堆，然后输出 Top K 就ok啦。

## Code

### Python

```python
import heapq
from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        power = [(sum(val), idx) for idx, val in enumerate(mat)]
        heapq.heapify(power)
        return [heapq.heappop(power)[1] for _ in range(k)]
```