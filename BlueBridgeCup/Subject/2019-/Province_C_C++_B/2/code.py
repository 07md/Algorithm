if __name__ == '__main__':
	num = 2019
	while num:
		print(chr(num % 26 + ord('A') - 1), end='')
		num = num // 26
