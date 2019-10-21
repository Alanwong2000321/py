'''
描述：一个网格迷宫由n行m列的单元格组成，每个单元格要么是空地（用0表示），要么是障碍物（用1来表示）。你的任务是找一条从起点到终点的最短步数和移动序列，其中UDLR表示上下左右操作。任何时候都不能在障碍物格子中，也不能走到迷宫之外。起点和终点保证都是空地。n，m<100。

测试：迷宫地图为
————————————————
版权声明：本文为CSDN博主「suljaxm」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/suljaxm/article/details/79636121

测试：迷宫地图为
       0 0 0 0 0 0 0 0
       0 1 1 1 1 0 1 0
       0 0 0 0 1 0 1 0
       0 1 0 0 0 0 1 0
       0 1 0 1 1 0 1 0
       0 1 0 0 0 0 1 1
       0 1 0 0 1 0 0 0


迷宫大小 n=m=8  起点为(0,0), 终点为(7,7) ，最后输出结果为

14

迷宫行走方式['D', 'D', 'R', 'R', 'D', 'D', 'D', 'R', 'R', 'R', 'D', 'R', 'R', 'D']
'''

mmap = [[0,0,0,0,0,0,0,0],
       [0,1,1,1,1,0,1,0],
       [0,0,0,0,1,0,1,0],
       [0,1,0,0,0,0,1,0],
       [0,1,0,1,1,0,1,0],
       [0,1,0,0,0,0,1,1],
       [0,1,0,0,1,0,0,0],
       [0,1,1,1,1,1,1,0]]
nrow, ncol = 8, 8
startx, starty = (0, 0)
endx, endy = (7, 7)
xx =[1,0,0,-1]     #右、下、左、上
yy =[0,1,-1,0]

vis = []
for i in range(0, 10):
    vis += [[]]
    for j in range(0, 10):
        vis[i] += [False]

state = (startx, starty, 0)
vis[startx][starty] = True
q = []
q.append(state)
path = []

while q:
    now = q.pop(0)
    nowx, nowy, step = now
    if nowx == endx and nowy == endy:
        print(f'到达终点， 经过{step}步')
        break
    for i in range(0, 4):
        newx = nowx + xx[i]
        newy = nowy + yy[i]
        newstep = step + 1
        newstate = (newx, newy, newstep)

        if newx < 0 or newy < 0 or newx >= nrow or newy >= ncol or vis[newx][newy] == True or mmap[newx][newy] == 1:  # 下标越界或者访问过或者是障碍物
            continue
        q.append(newstate)
        vis[newx][newy] = True