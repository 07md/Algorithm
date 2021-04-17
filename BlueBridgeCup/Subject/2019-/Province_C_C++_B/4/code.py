def judge(num):
	strList = list(str(num))
	return False if '2' in strList or '4' in strList else True


if __name__ == '__main__':
	ans = 0
	for i in range(1, 2019):
		if judge(i):
			for j in range(i + 1, 2019):
				if judge(j) and (2019 - i - j) > j and judge(2019 - i - j):
					ans += 1
					print(f'ans = {ans}, {i} + {j} + {2019 - i - j} = 2019')
	print(ans)
