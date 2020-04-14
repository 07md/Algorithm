import string


# a_s = string.ascii_lowercase[:19]
"""19本来就是奇数个，每次删除奇数位之后还是奇数个，所以只在19位之内模拟也是可以的。"""
a_s = string.ascii_lowercase[:19] * 106
while len(a_s) > 1:
    for i in range(len(a_s)):
        if i & 1:
            a_s = a_s[:i] + a_s[i + 1:]
print(a_s)
