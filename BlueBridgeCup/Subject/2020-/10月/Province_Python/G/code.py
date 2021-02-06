word = input()
count = {}
for a in word:
    if not count.get(a, None):
        count[a] = 1
    else:
        count[a] += 1

count = sorted(count.items(), key=lambda x: x[1])[-1]
print(f"{count[0]}\n{count[1]}")
