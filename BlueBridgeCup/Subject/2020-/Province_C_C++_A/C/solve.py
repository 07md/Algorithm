"""
1  B  6  7  15 16 28 29 45 46
3  5  8  14 17 27 30 44
4  9  13 18 26 31 43
10 12 19 25 32 42
11 20 24 33 41
21 23 34 40
22 35 39
36 38
37

1    B    3     4     5
1 -> 5 -> 13 -> 25 -> 41
  +4   +8   +12   +16
"""
if __name__ == '__main__':
    ans = 1
    for i in range(20):
        ans += i * 4
    print(ans)
