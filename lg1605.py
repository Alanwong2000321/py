n, m, t = [int(x) for x in input().split()]
grid = [[0] * m for x in range(n)]
used = [[False] * m for x in range(n)]
sx, sy, ex, ey = [int(x) for x in input().split()]
for _ in range(t):
  x, y = [int(x) for x in input().split()]
  grid[x-1][y-1] = 1
result = 0

dirs = ((0, 1), (0, -1), (1, 0), (-1, 0))
def dfs(x, y):
  global used, result
  if ex - 1 == x and ey - 1 == y:
    result += 1
    return
  for d in dirs:
    nx, ny = x + d[0], y + d[1]
    if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and (not used[nx][ny]):
      used[nx][ny] = True
      dfs(nx, ny)
      used[nx][ny] = False
used[sx-1][sy-1] = True
dfs(sx - 1, sy - 1)
print(result)