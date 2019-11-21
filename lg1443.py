n, m, sx, sy = [int(x) for x in input().split()]
grids = [[0] * m for x in range(n)]
used = [[False] * m for x in range(n)]
stepm = [[-1] * m for x in range(n)]
dirs = ((2, 1), (2, -1), (1, 2), (1, -2), (-2, 1), (-2, -1), (-1, 2), (-1, -2))
used[sx-1][sy-1] = True
queue = [(sx - 1, sy - 1, 0)]
stepm[sx-1][sy-1] = 0
while queue:
  s = queue.pop(0)
  for d in dirs:
    nx, ny, step = s[0] + d[0], s[1] + d[1], s[2]
    if 0 <= nx < n and 0 <= ny < m and (not used[nx][ny]):
      used[nx][ny] = True
      queue.append((nx, ny, step + 1))
      stepm[nx][ny] = step + 1

for line in stepm:
  for x in line:
    print("%-5d" % x, end="")
  print()
