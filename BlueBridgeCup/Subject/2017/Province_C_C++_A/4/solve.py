def dfs(x: int, y: int):
    if x == 0 or y == 0 or x == 6 or y == 6:
        global ans
        ans += 1
        return

    vis[x][y] = True
    vis[6 - x][6 - y] = True
    for dx, dy in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nx, ny = x + dx, y + dy
        if nx < 0 or ny < 0 or nx > 6 or ny > 6:
            continue
        if not vis[nx][ny]:
            dfs(nx, ny)
    vis[x][y] = False
    vis[6 - x][6 - y] = False


if __name__ == '__main__':
    ans = 0
    maps = [[0 for _ in range(7)] for _ in range(7)]
    vis = [[False for _ in range(7)] for _ in range(7)]
    dfs(3, 3)
    print(ans // 4)
