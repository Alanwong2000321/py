mmap = [[0,0,0,0,0,0,0,0],
       [0,1,1,1,1,0,1,0],
       [0,0,0,0,1,0,1,0],
       [0,1,0,0,0,0,1,0],
       [0,0,0,1,1,0,1,0],
       [0,0,0,0,0,0,1,1],
       [0,1,0,0,1,0,0,0],
       [0,1,1,1,1,1,1,0]]
nrow, ncol = 8, 8
dx = [1,0,-1,0]
dy = [0,1,0,-1]
vis = [[False] * 8 for i in range(8)]
res = 0
def dfs(x,y,step):
    global res
    if x == 4 and y == 2:
        print(f'到达终点， 经过{step}步')
        res = max(res, step)
        return
    step = step + 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < 8 and ny >= 0 and ny < 8 and vis[nx][ny] == False and mmap[nx][ny] == 0:
            vis[nx][ny] = True
            dfs(nx,ny,step)
            vis[nx][ny] = False
dfs(0,0,0)
print(res)