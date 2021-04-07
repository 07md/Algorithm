from itertools import permutations
from math import comb


def solve():
    container = set()
    string = "abbccc"
    cnt = 0
    for s in permutations(string):
        for item in container:
            if "".join(s) in item:
                break
        else:
            print(s)
            tmp = "".join(s) + "".join(s)
            container.add(tmp)
            container.add(reversed(tmp))
            cnt += 1
    print(cnt)


if __name__ == '__main__':
    solve()

    r, w, h, n = 1, 2, 3, 6
    print(((comb(n, r) * comb(n - r, w)) // n +
          (comb((n - 2) // 2, (h - 1) // 2) * comb((n - h - 1) // 2, w // 2))) // 2)
