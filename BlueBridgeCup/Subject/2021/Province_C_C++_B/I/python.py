if __name__ == '__main__':
	n, m = map(int, input().split())
	nums = [i + 1 for i in range(n)]
	seq = []  # 用于存储操作序列
	for _ in range(m):
		p, q = map(int, input().split())
		if p == 1 and seq:    # seq 不为空保证这是有一个 p = 0 之后的 p = 1 操作
			while seq and seq[-1][0] == 1:  # 如果是连续的 p = 1，只取最小的 q
				q = min(q, seq[-1][1])
			while len(seq) > 2 and seq[-2][1] >= q:  # 如果此次后缀升序的左边界小于上一次后缀升序的有边界，可以省略在此之前的两次操作
				seq.pop()
				seq.pop()
			seq.append((1, q))
		elif p == 0:
			while seq and seq[-1][0] == 0:  # 如果是连续的 p = 0，只取最大的 q
				q = max(q, seq[-1][1])
			while len(seq) > 2 and seq[-2][1] <= q:  # 如果此次前缀逆序的右边界大于上一次前缀逆序的有边界，可以省略在此之前的两次操作
				seq.pop()
				seq.pop()
			seq.append((0, q))

	k, left, right = n, 1, n
	for i in range(1, len(seq)):
		if seq[i][0] == 0:
			while right > seq[i][1] and left <= right:
				nums[right - 1] = k
				right -= 1
				k -= 1
		else:
			while left < seq[i][1] and left <= right:
				nums[left - 1] = k
				left += 1
				k -= 1
		if left > right:
			break

	if len(seq) % 2 != 0:
		while left <= right:
			nums[left - 1] = k
			left += 1
			k -= 1
	else:
		nums[right - 1] = k
		right -= 1
		k -= 1

	for num in nums:
		print(num, end=' ')
