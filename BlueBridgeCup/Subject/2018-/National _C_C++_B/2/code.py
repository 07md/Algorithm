def dfs(index):
    if index == 30:
        global ans
        ans += 1
        return 

    if light[index - 1] == 0:
        light[index] = 1
        dfs(index + 1)
        light[index] = 0
    dfs(index + 1)


light = [0 for _ in range(30)]
ans = 0
dfs(0)
print(ans)
