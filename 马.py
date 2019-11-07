nums = [int(x) for x in input().split()]
nrow, ncol = nums[0], nums[1]
startx, starty = (0, 0)#开始点

dic = [(-1, 2),(1, 2),(2, 1),(-2, 1),(2, -1),(-2, -1),(-1, -2),(1, -2)]
mmap = [[0] * nums[0] for i in range(nums[1])] 
vis = [[-1] * nums[0] for i in range(nums[1])]   
state=(startx, starty, 0)
vis[startx][starty] = 0
q = [state]

while q:
    now = q.pop(0)
    nowx, nowy, step = now
    for i in range(0,8):
        newx = nowx + dic[i][0]
        newy = nowy + dic[i][1]
        newstep = step + 1
        newstate = (newx, newy, newstep)
        if newx < 0 or newy < 0 or newx >= nrow or newy >= ncol or vis[newx][newy] >= 0:
            continue
        q.append(newstate)
        vis[newx][newy] = newstep

print("%-5d"%vis[0][0],"%-5d"%vis[0][1],"%-5d"%vis[0][2])
print("%-5d"%vis[1][0],"%-5d"%vis[1][1],"%-5d"%vis[1][2])
print("%-5d"%vis[2][0],"%-5d"%vis[2][1],"%-5d"%vis[2][2])